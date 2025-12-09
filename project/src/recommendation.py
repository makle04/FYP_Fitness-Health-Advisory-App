def give_recommendation(cluster_id):
    rec = {
        0: "Cluster 0: Low activity. Increase daily steps + start light exercise 3x/week.",
        1: "Cluster 1: Moderate activity. Add strength training + hydration tracking.",
        2: "Cluster 2: High performers. Focus on recovery, HIIT balancing, and sleep quality.",
        3: "Cluster 3: High BMI + moderate activity. Improve diet, start cardio + resistance combo.",
        4: "Cluster 4: Balanced fitness. Maintain routine, monitor heart rate improvements."
    }

    return rec.get(cluster_id, "No recommendation available.")
