from sqlalchemy import Column, DateTime, Integer, Text

from fever.db.base_class import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime)
    min_price = Column(Integer)
    max_price = Column(Integer)
