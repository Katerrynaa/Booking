from typing import Any, Dict
from fastapi import HTTPException

from src.schemas import CreateUser, BookFlight, BookHotel, HotelUpdate, UpdateUser
from src.models import User, SessionLocal, Flight, Hotel

import bcrypt
import requests
from dotenv import load_dotenv
import os

load_dotenv() 

flight_api_key = os.getenv("FLIGHT_API_KEY")
flight_url = os.getenv("FLIGHT_URL")

hotel_api_key = os.getenv("HOTEL_API_KEY")
hotel_url = os.getenv("HOTEL_URL")


class UserManager:
    @staticmethod
    def get_hashed_password(password: str):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password.decode()
    

    @staticmethod
    def create(user: CreateUser):
        with SessionLocal() as session:
            user = session.query(User).filter_by(email=user.email).first()
            if user:
                raise HTTPException(status_code=400, detail='Email has already been registered')

            hashed_password = UserManager.get_hashed_password(user.password)
            new_user = User(username=user.username, surname=user.surname, 
                            email=user.email, password=hashed_password)
            
            session.add(new_user)
            session.commit()


    @staticmethod
    def book_flight(data: BookFlight ):
        with SessionLocal() as session:
            data_dict = data.dict()
            obj = Flight(**data_dict)
            session.add(obj)
            session.commit()
            return obj
        

    @staticmethod
    def book_hotel(data: BookHotel):
        with SessionLocal() as session:
            data_dict = data.dict()
            obj = Hotel(**data_dict)
            session.add(obj)
            session.commit()
            return obj
           

    @staticmethod
    def get_flight(depature: str, arrival: str, limit: int) -> Dict[str, Any]:
        url = f"{flight_url}flights"
        params = {
            "access_key": flight_api_key,
            "dep_iata": depature,
            "arr_iata": arrival,
            "limit": limit
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching flight data")
        return response.json()
    

    @staticmethod
    def get_hotel(location: str, checkIn: str, checkOut: str, adults: int, 
                  currency: str, limit: int)  -> Dict[str, Any]:
        url = f"{hotel_url}"
        params = {
            "location": location,
            "checkIn": checkIn,
            "checkOut": checkOut,
            "adults": adults,
            "currency": currency,
            "limit": limit
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching hotel data")
        return response.json()
    

    @staticmethod
    def get_flight_id(flight_id):
        with SessionLocal() as session:
          return session.query(Flight).filter(Flight.id==flight_id).first()
        

    @staticmethod
    def delete_flight_by_id(flight_id):
        with SessionLocal() as session:
            obj = session.query(Flight).filter(Flight.id==flight_id).first()
            if obj:
                session.delete(obj)
                session.commit()
                return {"messsage": "This flight booking was deleted successful"}
            else:
                raise HTTPException(status_code=404, detail="Flight with such ID not found")
        

    @staticmethod
    def get_hotel_id(hotel_id):
        with SessionLocal() as session:
          return session.query(Hotel).filter(Hotel.id==hotel_id).first()
        
        
    @staticmethod
    def delete_hotel_by_id(hotel_id):
        with SessionLocal() as session:
            obj = session.query(Hotel).filter(Hotel.id==hotel_id).first()
            if obj:
                session.delete(obj)
                session.commit()
                return {"messsage": "This hotel booking was deleted successful"}
            else:
                raise HTTPException(status_code=404, detail="Hotel with such ID not found")
            

    @staticmethod
    def update_hotel_booking(hotel_id, data: HotelUpdate):
        with SessionLocal() as session:
            obj = session.query(Hotel).filter(Hotel.id==hotel_id).first()
            if obj:
                obj.checkIn = data.checkIn
                obj.checkOut = data.checkOut
                obj.adults = data.adults
                obj.children = data.children

                session.commit()
                session.refresh(obj)
                return obj 
            else:
                raise HTTPException(status_code=404, detail="Error hotel fetching data")


    @staticmethod
    def update_user_profile(user_id, data: UpdateUser):
        with SessionLocal() as session:
            obj = session.query(User).filter(User.id==user_id).first()
            if obj:
                obj.username = data.username 
                obj.surname = data.surname 
                obj.email = data.email 
                obj.password = data.password

                session.commit()
                session.refresh(obj)
                return obj 
            else:
                raise HTTPException(status_code=404, detail="Error user fetching data")
        
                
        


            

            






    





