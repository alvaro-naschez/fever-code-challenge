from datetime import date, time

import pytest

from fever.api.use_cases import get_events
from fever.models import Event


@pytest.fixture
def event1(str_to_datetime):
    return {
        "id": 291,
        "title": "Camela en concierto",
        "start_date": str_to_datetime("2021-06-30T21:00:00"),
        "end_date": str_to_datetime("2021-06-30T22:00:00"),
        "min_price": 1500,
        "max_price": 3000,
    }


@pytest.fixture
def event2(str_to_datetime):
    return {
        "id": 322,
        "title": "Pantomima Full",
        "start_date": str_to_datetime("2021-02-10T20:00:00"),
        "end_date": str_to_datetime("2021-02-10T21:30:00"),
        "min_price": 5500,
        "max_price": 5500,
    }


@pytest.fixture
def event3(str_to_datetime):
    return {
        "id": 1591,
        "title": "Los Morancos",
        "start_date": str_to_datetime("2021-07-31T20:00:00"),
        "end_date": str_to_datetime("2021-07-31T21:00:00"),
        "min_price": 6500,
        "max_price": 7500,
    }


def test_get_events(session, str_to_datetime, event1, event2, event3):
    session.add_all(
        [
            Event(**event1),
            Event(**event2),
            Event(**event3),
        ]
    )
    events = get_events(
        str_to_datetime("2021-06-30T20:00:00"),
        str_to_datetime("2021-07-31T22:00:00"),
        session,
    )
    events = [event.dict() for event in events.events]
    expected = [event1, event3]
    for event in expected:
        s, e = event["start_date"], event["end_date"]
        event["start_date"] = date(s.year, s.month, s.day)
        event["start_time"] = time(s.hour, s.minute, s.second)
        event["end_date"] = date(e.year, e.month, e.day)
        event["end_time"] = time(e.hour, e.minute, e.second)
        event["min_price"] = float(event["min_price"] / 100)
        event["max_price"] = float(event["max_price"] / 100)
    assert sorted(events, key=lambda e: e["id"]) == sorted(
        expected, key=lambda e: e["id"]
    )
