from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os

router = APIRouter()

DOWNLOAD_FILE = "predictions/latest_prediction.csv"


@router.get("/download/")
async def download_prediction():

    if not os.path.exists(DOWNLOAD_FILE):
        raise HTTPException(
            status_code=404,
            detail="Prediction file not found."
        )

    return FileResponse(
        DOWNLOAD_FILE,
        media_type="text/csv",
        filename="Inventory_Prediction.csv"
    )