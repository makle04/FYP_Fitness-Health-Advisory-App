import pandas as pd

df = pd.read_csv("project/data/output_with_activity_levels.csv")

samples = df[df["cluster"] != -1].groupby("cluster").sample(1)

for _, row in samples.iterrows():

    print("\n==============================")
    print(f"Cluster {int(row['cluster'])}")
    print("------------------------------")

    print(f"Age: {round(row['Age'],2)}")
    print(f"Weight_kg: {row['Weight_kg']}")
    print(f"Height_m: {row['Height_m']}")
    print(f"Session_Duration_hours: {row['Session_Duration_hours']}")
    print(f"Calories_Burned: {row['Calories_Burned']}")
    print(f"Max_BPM: {row['Max_BPM']}")
    print(f"Resting_BPM: {row['Resting_BPM']}")
    print(f"Avg_BPM: {row['Avg_BPM']}")
    print(f"Water_Intake_liters: {row['Water_Intake_liters']}")