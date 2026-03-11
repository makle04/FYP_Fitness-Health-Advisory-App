def generate_recommendations(df):

    # Cluster groups
    beginner_clusters = [3, 4]
    moderate_clusters = [0, 2, 6, 10]
    endurance_clusters = [5, 7, 8]
    hiit_clusters = [1, 9]

    def recommend(cluster):

        if cluster == -1:
            return "General fitness improvement recommended."

        elif cluster in beginner_clusters:
            return "Beginner-friendly workouts focusing on light cardio, mobility, and building consistency."

        elif cluster in moderate_clusters:
            return "Balanced cardio and strength training routine for steady and sustainable fitness improvement."

        elif cluster in endurance_clusters:
            return "Endurance-focused training with longer cardio sessions and attention to pacing and recovery."

        elif cluster in hiit_clusters:
            return "High-intensity interval training with strength conditioning and proper recovery."

        else:
            return "General fitness training plan."

    df["recommendation"] = df["cluster"].apply(recommend)

    return df["recommendation"]