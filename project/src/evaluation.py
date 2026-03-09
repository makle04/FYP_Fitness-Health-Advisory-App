import numpy as np

MIN_CLUSTERS = 3
MAX_CLUSTERS = 15
MAX_NOISE_RATIO = 0.55

def clustering_score(labels):
    total = len(labels)
    noise_ratio = np.sum(labels == -1) / total
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)

    if n_clusters < MIN_CLUSTERS or n_clusters > MAX_CLUSTERS:
        return -1
    if noise_ratio > MAX_NOISE_RATIO:
        return -1

    return n_clusters * (1 - noise_ratio)

def summarize(labels):
    return {
        "clusters": len(set(labels)) - (1 if -1 in labels else 0),
        "noise_ratio": round((labels == -1).sum() / len(labels), 3)
    }
