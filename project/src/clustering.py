from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Train K-Means
def run_kmeans(data, k):
    # Indent everything inside the function
    model = KMeans(n_clusters=k, random_state=42)
    labels = model.fit_predict(data)
    
    score = silhouette_score(data, labels)
    
    return labels, model, score
