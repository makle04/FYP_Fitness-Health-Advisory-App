import umap
import hdbscan
import numpy as np

def run_umap_hdbscan(
    data,
    n_neighbors: int,
    min_cluster_size: int,
    random_state: int = 42
):
    reducer = umap.UMAP(
        n_components=5,
        n_neighbors=n_neighbors,
        random_state=random_state,
        n_jobs=1
    )
    embedding = reducer.fit_transform(data)

    clusterer = hdbscan.HDBSCAN(
        min_cluster_size=min_cluster_size,
        metric="euclidean"
    )
    labels = clusterer.fit_predict(embedding)

    return labels, embedding
