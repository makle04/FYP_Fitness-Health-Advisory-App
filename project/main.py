from src.preprocessing import load_data, preprocess
from src.clustering import run_kmeans
from src.recommendation import give_recommendation


# STEP 1 — Load dataset
file_path = 'data/your_dataset.csv'
df = load_data(file_path)


# STEP 2 — Preprocess data
processed_data, cols = preprocess(df)


# STEP 3 — Run clustering (try k=3–6)
best_k = None
best_score = -1
best_labels = None
best_model = None


for k in range(3, 7):
labels, model, score = run_kmeans(processed_data, k)
print(f"K={k}, Silhouette Score={score}")


if score > best_score:
best_score = score
best_k = k
best_labels = labels
best_model = model


print("Best K:", best_k)


df['cluster'] = best_labels


# STEP 4 — Generate recommendations
df['recommendation'] = df['cluster'].apply(give_recommendation)


# STEP 5 — Save results
output_path = 'data/output_with_clusters.csv'
df.to_csv(output_path, index=False)
print("Saved results to", output_path)