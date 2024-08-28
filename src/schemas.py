from pydantic import BaseModel
from datetime import date, time

class CreateUser(BaseModel):
    username: str 
    surname: str 
    email: str 
    password: str 


class UpdateUser(BaseModel):
    username: str 
    surname: str 
    email: str 
    password: str 


class BookFlight(BaseModel):
    depature: str
    arrival: str 
    date: date
    time: time
    adults: int
    children: int
    bag: int


class BookHotel(BaseModel):
    city: str
    checkIn: date 
    checkOut: date 
    adults: int 
    children: int 
    payment_currency: str 


class HotelUpdate(BaseModel):
    checkIn: date
    checkOut: date 
    adults: int 
    children: int 