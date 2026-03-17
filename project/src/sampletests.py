import pandas as pd
import joblib

MODEL_PATH = "project/models/cluster_model.pkl"

FEATURES = [
    "Age",
    "BMI_fixed",
    "Intensity",
    "HRR",
    "BPM_Efficiency",
    "Hydration_Ratio",
    "Session_Duration_hours",
    "Calories_Burned"
]

# Load model
model = joblib.load(MODEL_PATH)


def predict_cluster(age, weight, height, session, calories, max_bpm, resting_bpm, avg_bpm, water):

    # Feature engineering (same as your API)
    bmi = weight / (height ** 2)
    hrr = max_bpm - resting_bpm
    intensity = avg_bpm / max_bpm
    bpm_eff = calories / avg_bpm
    hydration = water / session

    X = pd.DataFrame([{
        "Age": age,
        "BMI_fixed": bmi,
        "Intensity": intensity,
        "HRR": hrr,
        "BPM_Efficiency": bpm_eff,
        "Hydration_Ratio": hydration,
        "Session_Duration_hours": session,
        "Calories_Burned": calories
    }])

    cluster = model.predict(X)[0]

    return cluster


# -----------------------------
# INPUT YOUR TEST DATA HERE
# -----------------------------

tests = [
    ("Test 1", 53, 64.4, 1.58, 1.82, 1144, 198, 74, 158, 3.0),
    ("Test 2", 28, 62.4, 1.56, 2.0, 861, 193, 55, 141, 3.6),
    ("Test 3", 31, 100.0, 1.75, 1.46, 1573, 190, 67, 169, 1.0),

    # Low activity / beginner
    ("Test 4", 55, 85, 1.65, 0.5, 150, 140, 80, 100, 0.7),

    # Moderate fitness
    ("Test 5", 40, 78, 1.72, 1.0, 400, 170, 65, 130, 1.5),

    # High endurance
    ("Test 6", 29, 70, 1.80, 2.2, 900, 190, 55, 160, 2.5),

    # Short intense workout
    ("Test 7", 24, 68, 1.75, 0.7, 500, 185, 60, 155, 1.2),

    # Heavy + high effort
    ("Test 8", 45, 95, 1.70, 1.5, 800, 175, 75, 140, 2.0),

    # Very fit athlete
    ("Test 9", 26, 65, 1.78, 2.5, 1100, 200, 50, 170, 3.0),

    # Low calories / light workout
    ("Test 10", 50, 80, 1.68, 0.8, 250, 150, 70, 110, 1.0),

    # High BPM efficiency
    ("Test 11", 35, 72, 1.75, 1.2, 600, 180, 60, 150, 2.0),

    # Low hydration case
    ("Test 12", 38, 85, 1.70, 1.0, 500, 175, 65, 135, 0.5),

    # High hydration endurance
    ("Test 13", 32, 68, 1.82, 1.8, 850, 190, 58, 155, 3.5),

    # Extreme calorie burn
    ("Test 14", 30, 75, 1.78, 2.3, 1400, 195, 55, 165, 3.2),

    # Low intensity steady
    ("Test 15", 48, 82, 1.70, 1.5, 300, 150, 75, 110, 1.8)
]

# -----------------------------
# RUN TESTS
# -----------------------------

for name, age, weight, height, session, calories, max_bpm, resting_bpm, avg_bpm, water in tests:
    cluster = predict_cluster(age, weight, height, session, calories, max_bpm, resting_bpm, avg_bpm, water)
    print(f"{name}: Cluster {cluster}")