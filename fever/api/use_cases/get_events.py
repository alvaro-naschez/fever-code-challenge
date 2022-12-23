from datetime import datetime

from sqlalchemy.orm import Session

from fever.models import Event
from fever.schemas import EventList, EventSummary


def get_events(starts_at: datetime, ends_at: datetime, session: Session) -> EventList:
    try:
        events = (
            session.query(Event)
            .filter(Event.start_date >= starts_at, Event.end_date < ends_at)
            .all()
        )
    except Exception as err:
        session.close()
        raise err

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
