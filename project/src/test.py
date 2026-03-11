import pandas as pd

df = pd.read_csv("project/data/output_with_activity_levels.csv")

print(df["cluster"].value_counts().sort_index())