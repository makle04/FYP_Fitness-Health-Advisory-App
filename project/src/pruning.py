import pandas as pd

def prune_unrealistic_records(df):
    df = df.copy()

    numeric_cols = [
        "Age",
        "Weight_kg",
        "Height_m",
        "Max_BPM",
        "Avg_BPM",
        "Resting_BPM",
        "Session_Duration_hours",
        "Calories_Burned",
        "Water_Intake_liters"
    ]

    # ---------------------------------
    # Force numeric conversion
    # ---------------------------------
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows with missing critical values
    df = df.dropna(subset=numeric_cols)

    # ---------------------------------
    # Physiological pruning rules
    # ---------------------------------
    df = df[
        (df["Age"].between(16, 80)) &
        (df["Resting_BPM"].between(30, 120)) &
        (df["Max_BPM"].between(100, 220)) &
        (df["Avg_BPM"].between(50, 200)) &
        (df["Session_Duration_hours"].between(0.25, 4)) &
        (df["Calories_Burned"].between(100, 2000)) &
        (df["Water_Intake_liters"].between(0.5, 6)) &
        (df["Height_m"] > 0) &
        (df["Weight_kg"] > 0)
    ]

    # ---------------------------------
    # Enforce heart rate consistency
    # ---------------------------------
    df = df[
        (df["Resting_BPM"] < df["Avg_BPM"]) &
        (df["Avg_BPM"] < df["Max_BPM"])
    ]

    return df
