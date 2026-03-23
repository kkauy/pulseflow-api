from fastapi import APIRouter

from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.services import calculate_score

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
async def predict(data: PredictionRequest):
    score = calculate_score(age=data.age, bmi=data.bmi)
    return PredictionResponse(score=score)