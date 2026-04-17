import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

df = pd.read_csv("project/data/output_with_activity_levels.csv")

model = joblib.load("project/models/cluster_model.pkl")

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

# remove outliers
df = df[df["cluster"] != -1]

X = df[FEATURES]
y_true = df["cluster"]

y_pred = model.predict(X)

accuracy = accuracy_score(y_true, y_pred)

print("Model accuracy:", accuracy*100)