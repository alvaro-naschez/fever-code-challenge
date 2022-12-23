from datetime import datetime

from fastapi import APIRouter

from fever.api.use_cases import get_events
from fever.db.session import SlaveSession
from fever.schemas import EventList

router = APIRouter()


@router.get("/", response_model=EventList)
async def search(starts_at: datetime, ends_at: datetime):
    session = SlaveSession()
    return get_events(starts_at, ends_at, session)
