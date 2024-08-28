from fastapi import APIRouter, Depends
from typing import Annotated

from src.schemas import CreateUser, BookFlight, BookHotel, HotelUpdate, UpdateUser
from src.managers import UserManager
from src.auth import get_current_username


router = APIRouter()

@router.post("/create/user")
def create(schema: CreateUser):
    UserManager.create(schema)
    return {"message": "User has been created successfully!"}


@router.post("/book/flight")
def book_flight(data: BookFlight):
    UserManager.book_flight(data)
    return {"message": "Your flight booking has been created successful!"}


@router.post("/book/hotel")
def book_hotel(data: BookHotel):
    UserManager.book_hotel(data)
    return {"message": "Your hotel booking has been created successful!"}


@router.get("/auth/users")
def read_users(username: Annotated[str, Depends(get_current_username)]):
    return {"username": f"Hi {username}!"}


@router.get("/flights")
def get_flight(depature: str, 
               arrival: str,
               limit: int):
    return UserManager.get_flight(depature, arrival, limit)


@router.get("/hotels")
def get_hotel(location: str, 
              checkIn: str,
              checkOut: str, 
              adults: int, 
              currency: str, 
              limit: int):
    return UserManager.get_hotel(location, checkIn,
                                 checkOut, adults, 
                                 currency, limit)


@router.get("/flight/id")
def get_flight_id(flight_id):
    return UserManager.get_flight_id(flight_id)

@router.get("/hotel/id")
def get_hotel_id(hotel_id):
    return UserManager.get_hotel_id(hotel_id)


@router.delete("/delete/flight")
def delete_flight_by_id(flight_id):
    return UserManager.delete_flight_by_id(flight_id)


@router.delete("/delete/hotel")
def delete_hotel_by_id(hotel_id):
    return UserManager.delete_hotel_by_id(hotel_id)


@router.patch("/update/hotel/booking")
def update_hotel_booking(hotel_id, data: HotelUpdate):
    return UserManager.update_hotel_booking(hotel_id, data)


@router.put("/update/user")
def update_user_profile(user_id, data: UpdateUser):
    return UserManager.update_user_profile(user_id, data)

