import pandas as pd

# ==============================
# CONFIG
# ==============================
DATA_PATH = "project/data/gym_members_exercise_tracking_synthetic_data.csv"

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv(DATA_PATH)

print("\n==============================")
print("DATASET OVERVIEW")
print("==============================")

print(f"Number of samples: {df.shape[0]}")
print(f"Number of features: {df.shape[1]}")

print("\nColumn Names:")
print(df.columns.tolist())


# ==============================
# DATA TYPES
# ==============================
print("\n==============================")
print("DATA TYPES")
print("==============================")
print(df.dtypes)


# ==============================
# MISSING VALUES CHECK
# ==============================
print("\n==============================")
print("MISSING VALUES")
print("==============================")
missing = df.isnull().sum()
print(missing[missing > 0] if missing.sum() > 0 else "No missing values found.")


# ==============================
# BASIC STATISTICS
# ==============================
print("\n==============================")
print("NUMERICAL SUMMARY")
print("==============================")
print(df.describe())


# ==============================
# SAMPLE DATA
# ==============================
print("\n==============================")
print("SAMPLE DATA (FIRST 5 ROWS)")
print("==============================")
print(df.head())


# ==============================
# DOMAIN-SPECIFIC INSIGHTS
# ==============================
print("\n==============================")
print("KEY FEATURE INSIGHTS")
print("==============================")

if "Age" in df.columns:
    print(f"Average Age: {df['Age'].mean():.2f}")

if "Weight_kg" in df.columns:
    print(f"Average Weight: {df['Weight_kg'].mean():.2f} kg")

if "Height_m" in df.columns:
    print(f"Average Height: {df['Height_m'].mean():.2f} m")

if "Calories_Burned" in df.columns:
    print(f"Average Calories Burned: {df['Calories_Burned'].mean():.2f}")

if "Session_Duration_hours" in df.columns:
    print(f"Average Workout Duration: {df['Session_Duration_hours'].mean():.2f} hours")

if "Avg_BPM" in df.columns:
    print(f"Average Heart Rate: {df['Avg_BPM'].mean():.2f} BPM")

if "Water_Intake_liters" in df.columns:
    print(f"Average Water Intake: {df['Water_Intake_liters'].mean():.2f} L")


# ==============================
# DATA VALIDATION CHECKS
# ==============================
print("\n==============================")
print("DATA VALIDATION CHECKS")
print("==============================")

if all(col in df.columns for col in ["Resting_BPM", "Avg_BPM", "Max_BPM"]):
    invalid_hr = df[
        (df["Resting_BPM"] >= df["Avg_BPM"]) |
        (df["Avg_BPM"] >= df["Max_BPM"])
    ]
    print(f"Inconsistent heart rate records: {len(invalid_hr)}")

if "Age" in df.columns:
    unrealistic_age = df[(df["Age"] < 16) | (df["Age"] > 80)]
    print(f"Unrealistic age records: {len(unrealistic_age)}")


# ==============================
# CONCLUSION SUMMARY
# ==============================
print("\n==============================")
print("DATASET SUMMARY")
print("==============================")
print("The dataset contains structured fitness-related features including")
print("demographic, physiological, and activity-based attributes.")
print("This representation is suitable for machine learning applications,")
print("particularly clustering and pattern analysis.")