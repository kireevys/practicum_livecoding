from pydantic import BaseModel

from integrations.customer import Fine, get_customer


class Event:
    customer_id: str
    data: dict


class FineEvent(BaseModel):
    x: int
    y: str
    location: Geodata


class NewFineEvent:
    customer: id
    data: FineEvent


def _event_to_fine(event: FineEvent) -> Fine:
    pass


def fine_handler(event: FineEvent):
    fine = _event_to_fine(event)
    customer = get_customer(customer_id=event.customer_id)
    create_fine(fine)
