import logging
import warnings

from src.preprocessing import (
    load_data,
    standardise_columns,
    validate_columns,
    clean_and_scale
)
from src.feature_engineering import add_engineered_features
from src.pruning import prune_unrealistic_records
from src.clustering import run_umap_hdbscan
from src.evaluation import clustering_score, summarize
from src.recommendation import generate_recommendations

# ---------------------------------
# CONFIGURATION
# ---------------------------------
DATA_PATH = "data/gym_members_exercise_tracking_synthetic_data.csv"
OUTPUT_PATH = "data/output_with_activity_levels.csv"

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

# ---------------------------------
# SETUP
# ---------------------------------
warnings.filterwarnings("ignore")
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

# ---------------------------------
# MAIN PIPELINE
# ---------------------------------
def main():
    logging.info("Loading dataset")
    df = load_data(DATA_PATH)

    # Standardise column names
    df = standardise_columns(df)

    # Validate required columns exist
    validate_columns(df)

    # ---------------------------------
    # Pruning (realistic data cleaning)
    # ---------------------------------
    before = len(df)
    df = prune_unrealistic_records(df)
    after = len(df)
    logging.info(f"Pruned {before - after} unrealistic records")

    # ---------------------------------
    # Feature Engineering
    # ---------------------------------
    before = len(df)
    df = add_engineered_features(df)
    after = len(df)
    logging.info(f"Dropped {before - after} rows during feature engineering")

    # Remove extreme calorie outliers (top 1%)
    df = df[df["Calories_Burned"] < df["Calories_Burned"].quantile(0.99)]

    # ---------------------------------
    # Scaling
    # ---------------------------------
    df = clean_and_scale(df, FEATURES)

    # ---------------------------------
    # Clustering search
    # ---------------------------------
    best_score = -1
    best_labels = None
    best_params = None
    best_embedding = None

    logging.info("Searching best UMAP + HDBSCAN configuration")

    for n_neighbors in [10, 15, 20, 25]:
        for min_size in [10, 15, 20]:
            labels, embedding = run_umap_hdbscan(
                df[FEATURES],
                n_neighbors=n_neighbors,
                min_cluster_size=min_size
            )

            score = clustering_score(labels)

            if score > best_score:
                best_score = score
                best_labels = labels
                best_params = (n_neighbors, min_size)
                best_embedding = embedding

    # ---------------------------------
    # Fallback (guaranteed robustness)
    # ---------------------------------
    if best_labels is None:
        logging.warning(
            "No clustering configuration satisfied quality constraints. "
            "Applying fallback parameters."
        )

        best_labels, best_embedding = run_umap_hdbscan(
            df[FEATURES],
            n_neighbors=15,
            min_cluster_size=15
        )
        best_params = (15, 15)

    # ---------------------------------
    # Attach results
    # ---------------------------------
    df["cluster"] = best_labels

    logging.info(
        f"Selected parameters: "
        f"UMAP neighbors={best_params[0]}, "
        f"HDBSCAN min_cluster_size={best_params[1]}"
    )
    logging.info(f"Cluster summary: {summarize(best_labels)}")

    # ---------------------------------
    # Recommendations
    # ---------------------------------
    df["recommendation"] = generate_recommendations(df)

    # ---------------------------------
    # Save output
    # ---------------------------------
    df.to_csv(OUTPUT_PATH, index=False)
    logging.info(f"Saved results to {OUTPUT_PATH}")

# ---------------------------------
# ENTRY POINT
# ---------------------------------
if __name__ == "__main__":
    main()
