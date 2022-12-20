from datetime import datetime

from pydantic import BaseModel


class EventIn(BaseModel):
    id: int
    title: str
    start_date: datetime
    end_date: datetime
    max_price: float
    min_price: float
