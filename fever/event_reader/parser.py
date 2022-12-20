from typing import Any
from xml.etree.ElementTree import Element


def parse_event(xml_event: Element) -> dict[str, Any]:
    event_id = int(xml_event.attrib["base_event_id"])
    title = xml_event.get("title")
    event = xml_event[0]
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

    return event
