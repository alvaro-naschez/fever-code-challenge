from datetime import date, time

from .base import BaseModel


class EventSummary(BaseModel):
    id: int
    title: str
    start_date: date
    start_time: time | None = ...
    end_date: date | None = ...
    end_time: time | None = ...
    min_price: float | None = ...
    max_price: float | None = ...

    class Config:
        fields = {
            "id": {
                "description": "Identifier for the plan (integer)",
            },
            "title": {
                "description": "Title of the plan",
            },
            "start_date": {
                "description": "Date when the event starts in local time",
            },
            "start_time": {
                "description": "Time when the event starts in local time",
                "example": "22:38:19",
            },
            "end_date": {
                "description": "Date when the event ends in local time",
            },
            "end_time": {
                "description": "Time when the event ends in local time",
                "example": "14:45:15",
            },
            "min_price": {
                "description": "Min price from all the available tickets",
            },
            "max_price": {
                "description": "Max price from all the available tickets",
            },
        }
