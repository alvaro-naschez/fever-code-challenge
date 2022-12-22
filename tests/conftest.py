import pytest

from fever.db.session import MasterSession


@pytest.fixture(autouse=True)
def session(monkeypatch):
    session = MasterSession()
    session.autoflush = True
    monkeypatch.setattr(session, "commit", lambda: None)
    yield session
    session.close()
