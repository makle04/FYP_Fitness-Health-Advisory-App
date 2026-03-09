from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

df = pd.read_csv("project/data/output_with_activity_levels.csv")

features = [
"Age",
"BMI_fixed",
"Intensity",
"HRR",
"BPM_Efficiency",
"Hydration_Ratio",
"Session_Duration_hours"
]

df_clean = df[df["cluster"] != -1]

scaler = MinMaxScaler()
X = scaler.fit_transform(df_clean[features])

score = silhouette_score(X, df_clean["cluster"])

print("Silhouette Score:", score)

print("\nCluster distribution:")
print(df["cluster"].value_counts())

print("\nNoise ratio:", (df["cluster"] == -1).mean())