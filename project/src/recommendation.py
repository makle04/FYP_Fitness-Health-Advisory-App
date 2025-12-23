def generate_recommendations(df):
    cluster_means = df.groupby("cluster").mean(numeric_only=True)

    def recommend(row):
        cluster = row["cluster"]

        if cluster == -1:
            return "General fitness improvement recommended."

        intensity = cluster_means.loc[cluster, "Intensity"]

        if intensity >= 0.7:
            return "High-intensity training with focus on recovery and hydration."
        elif intensity >= 0.4:
            return "Balanced cardio and strength training program."
        else:
            return "Low-impact cardio with emphasis on consistency."

    return df.apply(recommend, axis=1)
