import pandas as pd
from sklearn.preprocessing import MinMaxScaler

REQUIRED_COLUMNS = [
    "Age", "Weight_kg", "Height_m",
    "Calories_Burned", "Session_Duration_hours",
    "Max_BPM", "Resting_BPM", "Avg_BPM",
    "Water_Intake_liters"
]

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def standardise_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.replace(" ", "_", regex=False)
        .str.replace("(kg)", "kg", regex=False)
        .str.replace("(m)", "m", regex=False)
        .str.replace("(hours)", "hours", regex=False)
        .str.replace("(liters)", "liters", regex=False)
    )
    return df

def validate_columns(df: pd.DataFrame):
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

def clean_and_scale(df: pd.DataFrame, feature_cols: list) -> pd.DataFrame:
    df = df.copy()

    for col in feature_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=feature_cols)

    scaler = MinMaxScaler()
    df[feature_cols] = scaler.fit_transform(df[feature_cols])

    return df

def clean_and_scale(df: pd.DataFrame, feature_cols: list) -> pd.DataFrame:
    df = df.copy()

    # Force numeric conversion
    for col in feature_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows with missing numeric values
    df = df.dropna(subset=feature_cols)

    scaler = MinMaxScaler()
    df[feature_cols] = scaler.fit_transform(df[feature_cols])

    return df