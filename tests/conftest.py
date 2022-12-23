from datetime import datetime

import pytest

from fever.db.base import Base
from fever.db.session import MasterSession
from fever.db.session import master_engine as engine

# create all tables and everything in test db
Base.metadata.create_all(bind=engine)


@pytest.fixture(autouse=True)
def session(monkeypatch):
    session = MasterSession()
    session.autoflush = True
    monkeypatch.setattr(session, "commit", lambda: None)
    yield session
    session.close()


@pytest.fixture
def str_to_datetime(autouse=True):
    datetime_format = "%Y-%m-%dT%H:%M:%S"

    def closure(dt):
        return datetime.strptime(dt, datetime_format)

    return closure
