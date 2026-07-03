import os
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)

PREDICTION_FOLDER = os.path.join(
    BASE_DIR,
    "..",
    "predictions"
)

os.makedirs(
    PREDICTION_FOLDER,
    exist_ok=True
)


def save_prediction(df):

    latest_file = os.path.join(
        PREDICTION_FOLDER,
        "latest_prediction.csv"
    )

    df.to_csv(
        latest_file,
        index=False
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    history_file = os.path.join(
        PREDICTION_FOLDER,
        f"prediction_{timestamp}.csv"
    )

    df.to_csv(
        history_file,
        index=False
    )

    return {
        "latest": latest_file,
        "history": history_file
    }