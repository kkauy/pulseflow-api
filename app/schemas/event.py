from datetime import datetime
from typing import Any, Dict, Literal
from pydantic import BaseModel

class EventIn(BaseModel):
    device_id: str
    user_id: str
    event_type: Literal["battery_low","device_online"]
    status: Literal["ok","warning"]
    severity: Literal["low","medium"]
    source: str
    event_time: datetime
    payload: Dict[str, Any]
