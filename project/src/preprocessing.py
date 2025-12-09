import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.decomposition import PCA

def load_data(path):
    df = pd.read_csv(path)
    return df

def preprocess(df, apply_pca=False, n_components=2):
    df = df.copy()

    # Standardize column names
    df.columns = df.columns.str.replace(" ", "_").str.replace("(kg)", "kg") \
                           .str.replace("(m)", "m").str.replace("(hours)", "hours") \
                           .str.replace("(liters)", "liters")

    # Ensure numeric columns are numeric and drop rows with missing values
    numeric_cols_to_convert = [
        "Max_BPM", "Resting_BPM", "Avg_BPM", "Calories_Burned",
        "Session_Duration_hours", "Weight_kg", "Height_m", "Water_Intake_liters"
    ]
    for col in numeric_cols_to_convert:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows where essential numeric columns are missing
    df = df.dropna(subset=numeric_cols_to_convert)

    # Recalculate BMI
    if "Weight_kg" in df.columns and "Height_m" in df.columns:
        df["BMI_fixed"] = df["Weight_kg"] / (df["Height_m"] ** 2)

    # Duration category
    if "Session_Duration_hours" in df.columns:
        df["Duration_Category"] = pd.cut(
            df["Session_Duration_hours"],
            bins=[0, 0.75, 1.5, 5],
            labels=["Short", "Medium", "Long"]
        )

    # Engineered features
    df["Intensity"] = df["Calories_Burned"] / df["Session_Duration_hours"]
    df["HRR"] = df["Max_BPM"] - df["Resting_BPM"]
    df["Hydration_Ratio"] = df["Water_Intake_liters"] / df["Weight_kg"]
    df["BPM_Efficiency"] = df["Avg_BPM"] / df["Max_BPM"]

    # Remove outliers in Calories_Burned
    if "Calories_Burned" in df.columns:
        df = df[df["Calories_Burned"] < df["Calories_Burned"].quantile(0.99)]

    # Handle categoricals
    if "Gender" in df.columns and "Workout_Type" in df.columns:
        df = pd.get_dummies(df, columns=["Gender", "Workout_Type"], drop_first=True)

    categorical_cols = df.select_dtypes(include=["object"]).columns
    encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    # Select numeric columns
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    numeric_df = df[numeric_cols].copy()

    # Fill missing values
    numeric_df = numeric_df.fillna(numeric_df.mean())

    # Scale features
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(numeric_df)

    # Optional PCA
    if apply_pca:
        pca = PCA(n_components=n_components)
        scaled_data = pca.fit_transform(scaled_data)

    return scaled_data, numeric_cols, encoders, df
