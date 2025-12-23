import pandas as pd

def add_engineered_features(df):
    df = df.copy()

    numeric_cols = [
        "Weight_kg", "Height_m", "Calories_Burned",
        "Session_Duration_hours", "Max_BPM",
        "Resting_BPM", "Avg_BPM", "Water_Intake_liters"
    ]

    # Ensure numeric BEFORE calculations
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=numeric_cols)

    df["BMI_fixed"] = df["Weight_kg"] / (df["Height_m"] ** 2)
    df["Intensity"] = df["Calories_Burned"] / df["Session_Duration_hours"]
    df["HRR"] = df["Max_BPM"] - df["Resting_BPM"]
    df["BPM_Efficiency"] = df["Avg_BPM"] / df["Max_BPM"]
    df["Hydration_Ratio"] = df["Water_Intake_liters"] / df["Weight_kg"]

    return df
