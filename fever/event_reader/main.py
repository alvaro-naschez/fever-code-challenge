import logging
from time import sleep

import httpx

from fever.config import settings
from fever.db.session import MasterSession
from fever.event_reader.use_cases import read_events


def main():
    logger = logging.getLogger(__name__)
    with MasterSession() as session:
        while True:
            r = httpx.get(settings.EVENTS_API_URL)

            if r.status_code != 200:
                sleep(1)
                continue

            read_events(r.content, session, logger)


if __name__ == "__main__":
    main()
