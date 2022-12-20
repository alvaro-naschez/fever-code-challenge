from .base import BaseModel
from .event_summary import EventSummary


class EventList(BaseModel):
    events: list[EventSummary]
