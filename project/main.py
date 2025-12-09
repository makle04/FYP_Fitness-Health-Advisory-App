import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import hdbscan
import umap
import numpy as np

file_path = r"C:\Users\joshu\OneDrive\Desktop\FYP_Fitness-Health-Advisory-App\project\data\gym_members_exercise_tracking_synthetic_data.csv"
output_path = r"C:\Users\joshu\OneDrive\Desktop\FYP_Fitness-Health-Advisory-App\project\data\output_with_activity_levels_hybrid.csv"

df = pd.read_csv(file_path)

# Standardize column names
df.columns = df.columns.str.replace(" ", "_").str.replace("(kg)", "kg") \
                       .str.replace("(m)", "m").str.replace("(hours)", "hours") \
                       .str.replace("(liters)", "liters")

# Ensure numeric columns are numeric
numeric_cols = ["Max_BPM", "Resting_BPM", "Avg_BPM", "Weight_kg", "Height_m",
                "Calories_Burned", "Session_Duration_hours", "Water_Intake_liters", "Age"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df = df.dropna(subset=numeric_cols)

# Recalculate BMI
df["BMI_fixed"] = df["Weight_kg"] / (df["Height_m"] ** 2)

# Engineered features
df["Intensity"] = df["Calories_Burned"] / df["Session_Duration_hours"]
df["HRR"] = df["Max_BPM"] - df["Resting_BPM"]
df["BPM_Efficiency"] = df["Avg_BPM"] / df["Max_BPM"]
df["Hydration_Ratio"] = df["Water_Intake_liters"] / df["Weight_kg"]

# Remove outliers
df = df[df["Calories_Burned"] < df["Calories_Burned"].quantile(0.99)]

# Scale numeric features
scaled_cols = ["Age", "BMI_fixed", "Intensity", "HRR", "BPM_Efficiency",
               "Hydration_Ratio", "Session_Duration_hours", "Calories_Burned"]
scaler = MinMaxScaler()
df[scaled_cols] = scaler.fit_transform(df[scaled_cols])

# Automatic UMAP + HDBSCAN tuning
best_n_clusters = 0
best_min_cluster_size = None
best_umap_neighbors = None
best_labels = None

umap_neighbors_options = [10, 15, 20, 25, 30]
min_cluster_size_options = [10, 15, 20, 25]

for n_neighbors in umap_neighbors_options:
    reducer = umap.UMAP(n_components=5, n_neighbors=n_neighbors, random_state=42)
    data_umap = reducer.fit_transform(df[scaled_cols])
    
    for min_size in min_cluster_size_options:
        clusterer = hdbscan.HDBSCAN(min_cluster_size=min_size, metric='euclidean')
        labels = clusterer.fit_predict(data_umap)
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        
        if n_clusters > best_n_clusters:  # prioritize more meaningful clusters
            best_n_clusters = n_clusters
            best_min_cluster_size = min_size
            best_umap_neighbors = n_neighbors
            best_labels = labels

# Apply best clustering
df['cluster'] = best_labels
print(f"Best UMAP neighbors: {best_umap_neighbors}, HDBSCAN min_cluster_size: {best_min_cluster_size}, Number of clusters: {best_n_clusters}")

# Map clusters to activity levels
cluster_stats = df.groupby('cluster')[['Intensity', 'Calories_Burned', 'Session_Duration_hours']].mean()

def map_cluster_to_activity(row):
    cluster = row['cluster']
    if cluster == -1:
        if row['Intensity'] >= df['Intensity'].quantile(0.75) and row['Calories_Burned'] >= df['Calories_Burned'].quantile(0.75):
            return "Very Active"
        elif row['Intensity'] >= df['Intensity'].quantile(0.5) and row['Calories_Burned'] >= df['Calories_Burned'].quantile(0.5):
            return "Active"
        elif row['Session_Duration_hours'] <= df['Session_Duration_hours'].quantile(0.25) and row['HRR'] <= df['HRR'].quantile(0.25):
            return "Less Active"
        else:
            return "Moderate"
    else:
        mean_intensity = cluster_stats.loc[cluster, "Intensity"]
        mean_calories = cluster_stats.loc[cluster, "Calories_Burned"]
        mean_duration = cluster_stats.loc[cluster, "Session_Duration_hours"]

        if mean_intensity >= df['Intensity'].quantile(0.75) and mean_calories >= df['Calories_Burned'].quantile(0.75):
            return "Very Active"
        elif mean_intensity >= df['Intensity'].quantile(0.5) and mean_calories >= df['Calories_Burned'].quantile(0.5):
            return "Active"
        elif mean_duration <= df['Session_Duration_hours'].quantile(0.25):
            return "Less Active"
        else:
            return "Moderate"

df['activity_level'] = df.apply(map_cluster_to_activity, axis=1)

# Simple recommendations
def recommend_workout(level):
    if level == "Very Active":
        return "High-intensity interval training 3-4x/week"
    elif level == "Active":
        return "Strength and cardio mix 3x/week"
    elif level == "Moderate":
        return "Moderate cardio 2-3x/week"
    else:
        return "Light exercise 1-2x/week"

df['recommendation'] = df['activity_level'].apply(recommend_workout)

# Save results
df.to_csv(output_path, index=False)
print("Saved results to", output_path)
print("Activity level distribution:\n", df[['activity_level', 'recommendation']].value_counts())
print("Sample clusters and assigned activity levels:")
print(df[['cluster', 'activity_level']].drop_duplicates().head(15))
