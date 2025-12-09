from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score

def run_dbscan(data, eps=0.3, min_samples=5):
    """
    DBSCAN clustering
    :param data: scaled (and optionally PCA-transformed) numeric data
    :param eps: neighborhood radius
    :param min_samples: minimum points to form a cluster
    :return: cluster labels, DBSCAN model, silhouette score (if applicable)
    """
    model = DBSCAN(eps=eps, min_samples=min_samples)
    labels = model.fit_predict(data)

    # Only compute silhouette if more than 1 cluster is found
    if len(set(labels)) > 1 and -1 not in set(labels):
        score = silhouette_score(data, labels)
    else:
        score = None  # silhouette not meaningful

    return labels, model, score
