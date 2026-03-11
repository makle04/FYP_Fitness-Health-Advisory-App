def generate_recommendations(df):

    cluster_recommendations = {

        -1: "General fitness improvement recommended.",

        0: "Balanced beginner workout focusing on light cardio and basic strength exercises.",

        1: "High-intensity interval training with explosive movements and adequate recovery.",

        2: "Moderate cardio combined with full-body resistance training.",

        3: "Beginner-friendly workouts focusing on mobility, flexibility, and light cardio.",

        4: "Low-impact exercises such as walking, cycling, or swimming to build endurance gradually.",

        5: "Longer endurance sessions such as steady-state running or cycling.",

        6: "Strength-focused workouts combined with moderate cardio training.",

        7: "Endurance conditioning with emphasis on pacing and aerobic capacity.",

        8: "Cardio-heavy endurance training with longer duration activities.",

        9: "Advanced HIIT training including sprint intervals and circuit strength training.",

        10: "Mixed training plan combining cardio, resistance training, and functional fitness.",

        11: "Short but intense workouts focusing on calorie burning and metabolic conditioning.",

        12: "Cardio-dominant fitness routine with emphasis on sustained heart rate and stamina.",

        13: "Strength and endurance hybrid program designed for high calorie expenditure and full-body conditioning."
    }

    df["recommendation"] = df["cluster"].map(cluster_recommendations)

    return df["recommendation"]