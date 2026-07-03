from fastapi import APIRouter
import pandas as pd

from services.predictor import predict
from services.inventory_analyzer import analyze_inventory
from services.csv_storage import save_prediction
from services.chatbot_services.faiss_service import (build_vector_store)

router = APIRouter()


@router.post("/")
def analyze():

    df = pd.read_csv(
        "uploads/latest_upload.csv"
    )

    predicted_df = predict(df)

    analyzed_df = analyze_inventory(
        predicted_df
    )

    save_prediction(
        analyzed_df
    )
    build_vector_store()

    summary = {
        "total_products": len(analyzed_df),

        "high_risk":
            len(
                analyzed_df[
                    analyzed_df["Risk"] == "High"
                ]
            ),

        "medium_risk":
            len(
                analyzed_df[
                    analyzed_df["Risk"] == "Medium"
                ]
            ),

        "low_risk":
            len(
                analyzed_df[
                    analyzed_df["Risk"] == "Low"
                ]
            )
    }

    table_data = analyzed_df.rename(
    columns={
        "Product ID": "product_id",
        "Product Name": "product_name",
        "Inventory Level": "stock",
        "Predicted Sales": "predicted_sales",
        "Daily Sales": "daily_sales",
        "Days Left": "days_left",
        "Risk": "risk",
        "Action": "action"
    }
    ).to_dict(orient="records")

    return {
    "message": "Analysis completed",
    "summary": summary,
    "table_data": table_data
}