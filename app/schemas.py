from datetime import datetime, date, time
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True


class FootballFieldBase(BaseModel):
    pass


class FootballFieldCreate(FootballFieldBase):
    pass


class FootballField(FootballFieldBase):
    id: int
    establishment_id: int

    class Config:
        orm_mode = True


class EstablishmentBase(BaseModel):
    pass


class EstablishmentCreate(EstablishmentBase):
    pass


class Establishment(EstablishmentBase):
    id: int
    username: str
    open_time: datetime
    close_time: datetime
    football_fields: List[FootballField] = []

    class Config:
        orm_mode = True


class EntrepreneurBase(BaseModel):
    email: str


class EntrepreneurCreate(EntrepreneurBase):
    password: str
    first_name: str
    last_name: str
    phone_number: str


class Entrepreneur(EntrepreneurBase):
    id: int
    first_name: str
    last_name: str
    phone_number: str
    establishments: List[Establishment] = []

    class Config:
        orm_mode = True


class BookingBase(BaseModel):
    pass


class BookingCreate(BookingBase):
    pass


class Status(str, Enum):
    a = 'a'
    b = 'b'
    c = 'c'


class Booking(BookingBase):
    id: int
    date: date
    time: time
    booking_date: date
    booking_time: time
    status: Status
    customer_id: int

    class Config:
        orm_mode = True


class CustomerBase(BaseModel):
    email: str


class CustomerCreate(CustomerBase):
    password: str


class Customer(CustomerBase):
    id: int
    username: str
    first_name: str
    last_name: str
    phone_number: str
    bookings: List[Booking]

    class Config:
        orm_mode = True
