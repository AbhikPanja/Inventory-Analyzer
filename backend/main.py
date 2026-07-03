from fastapi import FastAPI
from api.upload import router as upload_router
from api.analyze import router as analyze_router
from fastapi.middleware.cors import CORSMiddleware
from api.download import router as download_router
from api.chatbot import router as chatbot_router


app = FastAPI(title="Inventory Analyzer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    upload_router,
    prefix="/upload",
    tags=["Upload"]
)

app.include_router(
    analyze_router,
    prefix="/analyze",
    tags=["Analyze"]
)

app.include_router(download_router)

app.include_router(
    chatbot_router,
    prefix="/chat",
    tags=["Chatbot"]
)