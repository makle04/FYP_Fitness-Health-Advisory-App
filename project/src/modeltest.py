import pandas as pd
import joblib

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

samples = df[df["cluster"] != -1].groupby("cluster").sample(1)

for i,row in samples.iterrows():
    pred = model.predict([row[FEATURES]])[0]
    print("Actual:",row["cluster"],"Predicted:",pred)