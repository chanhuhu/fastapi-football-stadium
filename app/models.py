from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Numeric, Date, Time, Enum
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class FootballField(Base):
    __tablename__ = "football_fields"

    id = Column(Integer, primary_key=True, index=True)
    size = Column(Numeric(10, 2))
    price = Column(Numeric(10, 2))
    establishment_id = Column(Integer, ForeignKey("establishments.id"))

    establishment = relationship("Establishment", back_populates="football_fields")
    bookings = relationship("Booking", back_populates="football_field")


class Establishment(Base):
    __tablename__ = "establishments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    open_time = Column(DateTime)
    close_time = Column(DateTime)
    price_rate = Column(Numeric(10, 2))
    entrepreneur_id = Column(Integer, ForeignKey("entrepreneurs.id"))

    entrepreneur = relationship("Entrepreneur", back_populates="establishments")
    football_fields = relationship("FootballField", back_populates="establishment")


class Entrepreneur(Base):
    __tablename__ = "entrepreneurs"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    establishments = relationship("Establishment", back_populates="entrepreneur")


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    bookings = relationship("Bookings", back_populates="customers")


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    time = Column(Time)
    booking_date = Column(Date)
    booking_time = Column(Time)
    status = Column(Enum("a", "b"))
    football_field_id = Column(Integer, ForeignKey("football_fields.id"))
    customer_id = (Integer, ForeignKey("customers.id"))

    football_field = relationship("FootballField", back_populates="bookings")
