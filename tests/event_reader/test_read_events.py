from unittest.mock import MagicMock

from fever.event_reader.main import read_events
from fever.models import Event


def test_read_events(session, str_to_datetime):
    with open("./tests/resources/response1.xml") as xml_file:
        xml = xml_file.read()
    logger = MagicMock()
    read_events(xml, session, logger)
    assert session.query(Event.id).count() == 3
    event = session.query(Event).get(291)
    assert event.asdict() == {
        "id": 291,
        "title": "Camela en concierto",
        "start_date": str_to_datetime("2021-06-30T21:00:00"),
        "end_date": str_to_datetime("2021-06-30T22:00:00"),
        "min_price": 1500,
        "max_price": 3000,
    }
    event = session.query(Event).get(322)
    assert event.asdict() == {
        "id": 322,
        "title": "Pantomima Full",
        "start_date": str_to_datetime("2021-02-10T20:00:00"),
        "end_date": str_to_datetime("2021-02-10T21:30:00"),
        "min_price": 5500,
        "max_price": 5500,
    }
    event = session.query(Event).get(1591)
    assert event.asdict() == {
        "id": 1591,
        "title": "Los Morancos",
        "start_date": str_to_datetime("2021-07-31T20:00:00"),
        "end_date": str_to_datetime("2021-07-31T21:00:00"),
        "min_price": 6500,
        "max_price": 7500,
    }
    assert logger.debug.call_count == 3
    assert logger.error.call_count == 0
