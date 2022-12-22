from datetime import datetime
from unittest.mock import MagicMock

from fever.event_reader.main import read_events
from fever.models import Event


def test_read_events(session):
    with open("./tests/resources/response1.xml") as xml_file:
        xml = xml_file.read()
    logger = MagicMock()
    read_events(xml, session, logger)
    assert session.query(Event.id).count() == 3
    event = session.query(Event).filter(Event.id == 291).one()
    assert event.title == "Camela en concierto"
    datetime_format = "%Y-%m-%dT%H:%M:%S"
    assert event.start_date == datetime.strptime("2021-06-30T21:00:00", datetime_format)
    assert event.end_date == datetime.strptime("2021-06-30T22:00:00", datetime_format)
    assert event.min_price == 1500
    assert event.max_price == 3000
    event = session.query(Event).filter(Event.id == 322).one()
    assert event.title == "Pantomima Full"
    assert event.start_date == datetime.strptime("2021-02-10T20:00:00", datetime_format)
    assert event.end_date == datetime.strptime("2021-02-10T21:30:00", datetime_format)
    assert event.min_price == 5500
    assert event.max_price == 5500
    event = session.query(Event).filter(Event.id == 1591).one()
    assert event.title == "Los Morancos"
    assert event.start_date == datetime.strptime("2021-07-31T20:00:00", datetime_format)
    assert event.end_date == datetime.strptime("2021-07-31T21:00:00", datetime_format)
    assert event.min_price == 6500
    assert event.max_price == 7500
    assert logger.debug.call_count == 3
    assert logger.error.call_count == 0
