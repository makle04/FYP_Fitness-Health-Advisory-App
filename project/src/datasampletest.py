import pandas as pd

DATA_PATH = "project/data/output_with_activity_levels.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

# Count number of rows in each cluster
cluster_counts = df["cluster"].value_counts().sort_index()

print("\nCluster Distribution")
print("--------------------")

for cluster, count in cluster_counts.items():
    print(f"Cluster {cluster}: {count} samples")

print("\nTotal samples:", len(df))