from fastapi import APIRouter
from uuid import uuid4
from app.schemas.event import EventIn

router = APIRouter(prefix="/api/v1/events")

@router.post("")
def create_event(event: EventIn):
    return {
        "event_id": str(uuid4()),
        "message": "ok"
    }
