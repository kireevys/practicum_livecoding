import datetime
import uuid

from integrations.sender import Message


class Customer:
    id: str | None
    name: str
    number: str


def _gen_id() -> str:
    return str(uuid.uuid4())


def create_customer(customer_data: Customer):
    db.create(_gen_id(), *customer_data)


def get_customer(customer_id: str) -> Customer:
    return db.get(id=customer_id)


class Location:
    x: str
    y: str


class Fine:
    number: str
    date: datetime.date
    location: Location

@api_1
def create_fine_for_now():
    create_fine()

def create_fine(customer_id: str, fine: Fine):
    db.create(customer_id, fine)




class DbFine:
    pass


def _to_fine_from_db(db_fine: DbFine) -> Fine:
    pass


@api_v1(name="Получение начисленией", deprecated=True)
def get_fines(customer_id: str) -> list[Fine]:
    return [_to_fine_from_db(db_fine) for db_fine in db.filter(customer_id)]


class Paginated:
    __root__: list[Fine]
    per_page: int
    total: int
    title: str = default("Страница №0")

@api_2
def get_fines(customer_id: str) -> Paginated[Fine]:
    return [
        _to_fine_from_db(db_fine) for db_fine in db.filter(customer_id).limit().offset()
    ]


class DbCustomer:
    pass


def _to_customer_from_db(db_customer: DbCustomer) -> Customer:
    pass


def get_customers_who_need_fines() -> list[Customer]:
    return [_to_customer_from_db(db_customer) for db_customer in db.all()]


def send(customer: Customer, fine: Fine) -> uuid:
    Message(body=f"Вас пришел штраф №{fine.number}")
