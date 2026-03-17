from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

from src.feature_engineering import add_engineered_features
from src.recommendation import generate_recommendations

MODEL_PATH = "project/models/cluster_model.pkl"
SCALER_PATH = "project/models/scaler.pkl"

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

app = Flask(__name__)
CORS(app)

# Load model and scaler
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


@app.route("/")
def home():
    return "Fitness Health Advisory API Running"


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    df = pd.DataFrame([data])

    # Convert to numeric
    df = df.apply(pd.to_numeric, errors="coerce")

    # Feature engineering
    df = add_engineered_features(df)

    # Remove infinity
    df.replace([float("inf"), -float("inf")], 0, inplace=True)

    # Fill missing values
    df.fillna(0, inplace=True)

    # Scale features
# Scale features
    X_scaled = scaler.transform(df[FEATURES])

    # Restore feature names
    X_scaled = pd.DataFrame(X_scaled, columns=FEATURES)

    # Predict cluster
    cluster = model.predict(X_scaled)[0]

    df["cluster"] = cluster

    recommendation = generate_recommendations(df)[0]

    return jsonify({
        "cluster": int(cluster),
        "recommendation": recommendation
    })


if __name__ == "__main__":
    app.run(debug=True)