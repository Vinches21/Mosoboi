from dataclasses import dataclass


@dataclass
class Person:
    fio: str = None
    address: str = None
    phone: int = None
    email: str = None
    order_number: int = None
    order_date: int = None
    brand: str = None
    collection: str = None
    article: int = None
    part_number: int = None
    quantity: int = None
    deffect_quantity: int = None
    opened_quantity: int = None
    closed_quantity: int = None
    used_quantity: int = None
    message: str = None
    city: str = None