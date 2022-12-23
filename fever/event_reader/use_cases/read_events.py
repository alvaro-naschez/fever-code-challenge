import logging
import xml.etree.ElementTree as ET

from pydantic import ValidationError
from sqlalchemy.orm import Session

from fever.event_reader.parser import parse_event
from fever.models.event import Event
from fever.schemas import EventIn


def read_events(
    events_xml: str,
    session: Session,
    logger: logging.Logger,
    batch_size: int = 100,
):
    tree = ET.fromstring(events_xml)
    i = 0
    for base_event in tree.iter("base_event"):
        i += 1
        event = parse_event(base_event)
        try:
            event = EventIn(**event)
        except ValidationError as error:
            logger.error(f"Validation error, skipping event {event}")
            logger.error(error.errors())
            return

        logger.debug(event)
        session.merge(Event(**event.dict()))
        if i == batch_size:
            i = 0
            session.commit()
    session.commit()
