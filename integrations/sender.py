from enum import StrEnum
from uuid import UUID

from pydantic import BaseModel


class CustomerId:
    id: int


class CommunicationId:
    refer: UUID


class MessageType(StrEnum):
    EMAIL = "EMAIL"
    SMS = "SMS"
    PUSH = "PUSH"
    CALL = "CALL"


class CommunicationStatus(StrEnum):
    NEW = "NEW"
    SEND = "SEND"
    DELIVERED = "DELIVERED"
    READ = "READ"


class Message(BaseModel):
    body: str
    headers: str
    type: list[MessageType]


def _communication_factory(customer_id, message) -> CommunicationId:
    pass


def send_communication(customer_id: CustomerId, message: Message) -> CommunicationId:
    communication_id = _communication_factory(customer_id, message)
    return communication_id


class Delivery:
    delivery_type: MessageType
    status: CommunicationStatus


class DeliveryDetails:
    deliveries: list[Delivery]


class StatusResponse:
    status: CommunicationStatus
    delivery_details: DeliveryDetails


def get_communication_status(communication_id: CommunicationId) -> StatusResponse:
    status = _get_short_status(communication_id)
    details = _delivery_details(communication_id)
    return StatusResponse(status=status, details=details)


def cancel_communnication(communication_id: CommunicationId) -> CancelResponse:
    ...
