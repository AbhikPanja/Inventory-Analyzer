from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/")
async def upload_csv(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_DIR,
        "latest_upload.csv"
    )

    with open(file_path, "wb") as f:
        f.write(await file.read())

    return {
        "message": "Upload successful",
        "filename": "latest_upload.csv"
    }