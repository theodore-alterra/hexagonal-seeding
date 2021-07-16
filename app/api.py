from fastapi import APIRouter
from api.endpoints.billerScore.controller import router as billerScore
from api.endpoints.dataStream.controller import router as dataStream

api_router = APIRouter()

api_router.include_router(billerScore, prefix="/predict", tags=["Predict Biller Score"])
api_router.include_router(dataStream, prefix="/stream", tags=["Data Stream"])
