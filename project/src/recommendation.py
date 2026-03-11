def generate_recommendations(df):

    cluster_recommendations = {

        # Outliers
        -1: "General fitness improvement recommended.",

        # Beginner / low intensity
        3: "Beginner-friendly workouts focusing on building consistency with light cardio and mobility training.",
        4: "Low-impact endurance exercises such as walking, cycling, or swimming.",

        # Moderate balanced workouts
        0: "Balanced cardio and strength training routine to maintain overall fitness.",
        2: "Moderate cardio workouts combined with resistance training for steady progress.",
        6: "Mixed cardio and strength sessions to improve overall conditioning.",
        10: "Consistent moderate workouts focusing on sustainable long-term fitness.",

        # Endurance athletes
        5: "Long endurance training sessions with focus on hydration and pacing.",
        7: "Extended cardio sessions designed to improve stamina and aerobic capacity.",
        8: "Endurance-based workouts with emphasis on pacing strategies and recovery.",

        # High intensity athletes
        1: "High-intensity interval training with proper recovery and hydration.",
        9: "Advanced high-calorie burning workouts combining HIIT and strength conditioning."
    }

    df["recommendation"] = df["cluster"].map(cluster_recommendations)

    return df["recommendation"]