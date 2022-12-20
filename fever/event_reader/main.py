import xml.etree.ElementTree as ET
from datetime import datetime
from logging import getLogger
from time import sleep

import httpx

from fever.db.session import MasterSession
from fever.models.event import Event


def main():
    with MasterSession() as session:
        while True:
            r = httpx.get("https://provider.code-challenge.feverup.com/api/events")

            if r.status_code != 200:
                sleep(1)
                continue

            tree = ET.fromstring(r.content)

            BATCH_SIZE = 100
            i = 0
            for base_event in tree.iter("base_event"):
                i += 1
                event_id = int(base_event.attrib["base_event_id"])
                title = base_event.get("title")
                event = base_event[0]
                start_date = event.get("event_start_date")
                end_date = event.get("event_end_date")
                prices = [float(zone.get("price")) for zone in event.iter("zone")]
                max_price = int(max(prices) * 100)
                min_price = int(min(prices) * 100)

                event = {
                    "id": event_id,
                    "title": title,
                    "start_date": start_date,
                    "end_date": end_date,
                    "max_price": max_price,
                    "min_price": min_price,
                }

                try:
                    datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S")
                    datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S")
                except ValueError:
                    logger = getLogger(__name__)
                    logger.error(f"Error in datetime format, skipping event {event}")
                    continue

                print(event)
                session.merge(Event(**event))
                if i == BATCH_SIZE:
                    i = 0
                    session.commit()
            session.commit()


if __name__ == "__main__":
    main()
