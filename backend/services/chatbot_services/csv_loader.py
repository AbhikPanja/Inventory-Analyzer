import os
import pandas as pd

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

PREDICTION_FILE = os.path.join(
    BASE_DIR,
    "predictions",
    "latest_prediction.csv"
)

REQUIRED_COLUMNS = [
    "Product ID",
    "Product Name",
    "Inventory Level",
    "Predicted Sales",
    "Daily Sales",
    "Days Left",
    "Risk",
    "Recommended Order Quantity",
    "Supplier Name",
    "Supplier Lead Time",
    "Action"
]


def load_prediction_csv():

    if not os.path.exists(PREDICTION_FILE):
        raise FileNotFoundError(
            f"Prediction file not found:\n{PREDICTION_FILE}"
        )

    return pd.read_csv(PREDICTION_FILE)


def validate_dataframe(df):

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    return True


def get_inventory_data():

    df = load_prediction_csv()

    validate_dataframe(df)

    return df