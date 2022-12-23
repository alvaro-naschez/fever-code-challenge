from dataclasses import asdict, dataclass
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, Text

from fever.db.base_class import Base


@dataclass
class Event(Base):
    __tablename__ = "events"

    id: int = Column(Integer, primary_key=True)
    title: str = Column(Text, nullable=False)
    start_date: datetime = Column(DateTime, nullable=False)
    end_date: datetime = Column(DateTime)
    min_price: datetime = Column(Integer)
    max_price: datetime = Column(Integer)

    def asdict(self):
        return asdict(self)
