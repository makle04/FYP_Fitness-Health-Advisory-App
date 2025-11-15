import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_data(path):
df = pd.read_csv(path)
return df


def preprocess(df):
# Select numerical features
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
numeric_df = df[numeric_cols].copy()


# Handle missing values
numeric_df = numeric_df.fillna(numeric_df.mean())


# Scale data
scaler = StandardScaler()
scaled = scaler.fit_transform(numeric_df)


return scaled, numeric_cols