import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# CONFIG
# ==============================
DATA_PATH = "project/data/output_with_activity_levels.csv"
SAVE_PATH = "cluster_heatmap.png"

FEATURES = [
    "BMI_fixed",
    "Intensity",
    "HRR",
    "BPM_Efficiency",
    "Hydration_Ratio",
    "Session_Duration_hours",
    "Calories_Burned"
]

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv(DATA_PATH)

# Remove noise for clarity
df = df[df["cluster"] != -1]

# ==============================
# CLUSTER LABELS
# ==============================
cluster_names = {
    0: "Beginner Balanced",
    1: "High Intensity (HIIT)",
    2: "Moderate Fitness",
    3: "Beginner Mobility",
    4: "Low Impact",
    5: "Endurance Training",
    6: "Strength Focused",
    7: "Aerobic Conditioning",
    8: "Cardio Endurance",
    9: "Advanced HIIT",
    10: "Balanced Fitness",
    11: "Short Intense",
    12: "Sustained Cardio",
    13: "Hybrid Training"
}

df["cluster_name"] = df["cluster"].map(cluster_names)

# ==============================
# COMPUTE CLUSTER CENTROIDS
# ==============================
centroids = df.groupby("cluster_name")[FEATURES].mean()

# Optional: normalise for better comparison
centroids_normalized = (centroids - centroids.min()) / (centroids.max() - centroids.min())

# ==============================
# PLOT HEATMAP
# ==============================
plt.figure(figsize=(12, 8))

sns.heatmap(
    centroids_normalized,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Normalized Cluster Feature Profiles")
plt.xlabel("Features")
plt.ylabel("Cluster")

plt.tight_layout()
plt.savefig(SAVE_PATH, dpi=300)
plt.show()

print(f"\nHeatmap saved to: {SAVE_PATH}")