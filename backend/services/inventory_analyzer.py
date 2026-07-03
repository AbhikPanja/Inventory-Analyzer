import pandas as pd
import numpy as np


def calculate_risk(row):

    days_left = row["Days Left"]

    if days_left <= 15:
        return "High"

    elif days_left <= 35:
        return "Medium"

    return "Low"


def get_action(risk):

    if risk == "High":
        return "Urgent Reorder"

    elif risk == "Medium":
        return "Monitor Closely"

    return "Stock Sufficient"


def analyze_inventory(df):

    df = df.copy()

    df["Daily Sales"] = (
        df["Predicted Sales"] / 30
    ).round(2)

    df["Days Left"] = np.where(
        df["Daily Sales"] > 0,
        (df["Inventory Level"] /df["Daily Sales"]).round(1),999
    )

    df["Risk"] = df.apply(calculate_risk,axis=1)

    df["Recommended Order Quantity"] = (
        (df["Daily Sales"] * df["Supplier Lead Time"]* 2) - df["Inventory Level"]
    )

    df["Recommended Order Quantity"] = (
        df["Recommended Order Quantity"].clip(lower=0).round().astype(int)
    )

    df["Action"] = df["Risk"].apply(
        get_action
    )

    final_columns = [

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

    existing_columns = [
    col
    for col in final_columns
    if col in df.columns
    ]

    df = df[existing_columns]

    return df