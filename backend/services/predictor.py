import pandas as pd
import joblib

model = joblib.load(
    "models/inventory_model.pkl"
)

encoders = joblib.load(
    "models/encoders.pkl"
)

feature_columns = joblib.load(
    "models/feature_columns.pkl"
)


def prepare_features(df):

    df = df.copy()

    # Convert date
    df["Date"] = pd.to_datetime(df["Date"],format="%d/%m/%Y")
    # Create date features
    df["Month"] = df["Date"].dt.month
    df["Day"] = df["Date"].dt.day
    df["DayOfWeek"] = df["Date"].dt.dayofweek

    # Drop columns not used by model
    columns_to_drop = [
        "Date",
        "Product ID",
        "Product Name",
        "Supplier Name",
        "Supplier Lead Time"
    ]

    for col in columns_to_drop:
        if col in df.columns:
            df.drop(col, axis=1, inplace=True)

    # Encode categorical columns
    for col, encoder in encoders.items():

        unknown_values = set(df[col]) - set(encoder.classes_)

        if unknown_values:
            raise ValueError(
            f"Unknown values found in {col}: {unknown_values}"
        )

        df[col] = encoder.transform(df[col])

    # Keep exact training column order
    df = df[feature_columns]

    return df

def predict(df):

    original_df = df.copy()

    processed_df = prepare_features(df)

    predictions = model.predict(processed_df)
    predictions = predictions.clip(min=0)

    original_df["Predicted Sales"] = predictions.round().astype(int)

    return original_df


