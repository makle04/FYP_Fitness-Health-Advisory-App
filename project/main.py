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

DATA_PATH = "project/data/gym_members_exercise_tracking_synthetic_data.csv"
OUTPUT_PATH = "project/data/output_with_activity_levels.csv"

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

warnings.filterwarnings("ignore")
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def main():
    logging.info("Loading dataset")
    df = load_data(DATA_PATH)

    df = standardise_columns(df)

    validate_columns(df)

    before = len(df)
    df = prune_unrealistic_records(df)
    after = len(df)
    logging.info(f"Pruned {before - after} unrealistic records")

    before = len(df)
    df = add_engineered_features(df)
    after = len(df)
    logging.info(f"Dropped {before - after} rows during feature engineering")

    df = df[df["Calories_Burned"] < df["Calories_Burned"].quantile(0.99)]

    df = clean_and_scale(df, FEATURES)

    best_score = -1
    best_labels = None
    best_params = None
    best_embedding = None

    logging.info("Searching best UMAP + HDBSCAN configuration")

    for n_neighbors in [20, 30, 40]:
        for min_size in [25, 30, 35]:
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


    df["cluster"] = best_labels

    logging.info(
        f"Selected parameters: "
        f"UMAP neighbors={best_params[0]}, "
        f"HDBSCAN min_cluster_size={best_params[1]}"
    )
    logging.info(f"Cluster summary: {summarize(best_labels)}")


    df["recommendation"] = generate_recommendations(df)


    df.to_csv(OUTPUT_PATH, index=False)
    logging.info(f"Saved results to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
    