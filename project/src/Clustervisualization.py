import pandas as pd
import matplotlib.pyplot as plt
import umap

# ==============================
# CONFIG
# ==============================
DATA_PATH = "project/data/output_with_activity_levels.csv"
SAVE_PATH = "cluster_visualization.png"

FEATURES = [
    "Age",
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

X = df[FEATURES]
labels = df["cluster"]

# ==============================
# CLUSTER LABELS (BASED ON YOUR RECOMMENDATIONS)
# ==============================
cluster_names = {
    -1: "Noise / Irregular",
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
# UMAP REDUCTION
# ==============================
reducer = umap.UMAP(
    n_components=2,
    n_neighbors=15,
    random_state=42
)

embedding = reducer.fit_transform(X)

# ==============================
# PLOT (WITH INTERPRETABLE LABELS)
# ==============================
plt.figure(figsize=(12, 8))

for cluster_id in sorted(df["cluster"].unique()):
    subset = df[df["cluster"] == cluster_id]
    name = cluster_names.get(cluster_id, f"Cluster {cluster_id}")

    plt.scatter(
        embedding[subset.index, 0],
        embedding[subset.index, 1],
        s=20,
        alpha=0.8,
        label=name
    )

plt.title("Cluster Visualization with Interpreted Fitness Profiles")
plt.xlabel("UMAP Dimension 1")
plt.ylabel("UMAP Dimension 2")

plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=8)
plt.tight_layout()
plt.savefig(SAVE_PATH, dpi=300)
plt.show()

print(f"\nVisualization saved to: {SAVE_PATH}")