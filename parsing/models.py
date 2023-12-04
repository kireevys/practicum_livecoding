import decimal

from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: decimal.Decimal
    stock: int
    discount: float
