from datetime import datetime

from fastapi import APIRouter

from fever.db.session import SlaveSession
from fever.models import Event
from fever.schemas import EventList, EventSummary

router = APIRouter()


@router.get("/", response_model=EventList)
async def search(starts_at: datetime, ends_at: datetime):
    with SlaveSession() as session:
        events = (
            session.query(Event)
            .filter(Event.start_date >= starts_at, Event.end_date < ends_at)
            .all()
        )

    event_list = []
    for event in events:
        new_event = EventSummary(
            id=event.id,
            title=event.title,
            start_date=event.start_date.date(),
            start_time=event.start_date.time(),
            end_date=event.end_date.date(),
            end_time=event.end_date.time(),
            min_price=event.min_price / 100,
            max_price=event.max_price / 100,
        )
        event_list.append(new_event)

    return EventList(events=event_list)
