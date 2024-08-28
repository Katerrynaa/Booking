from sqlalchemy import String, Integer, Column, Date, Time, Date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv() 

engine = create_engine(os.getenv("DATABASE_URL"))
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    surname = Column(String(100))
    email = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)


class Flight(Base):
    __tablename__ = 'flights'

    id = Column(Integer, primary_key=True, index=True)
    depature = Column(String(100), nullable=False)
    arrival = Column(String(100), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    adults = Column(Integer, nullable=True)
    children = Column(Integer, nullable=True)
    bag = Column(Integer, nullable=False)


class Hotel(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(100), nullable=False)
    checkIn = Column(Date, nullable=False)
    checkOut = Column(Date, nullable=False)
    adults = Column(Integer, nullable=False)
    children = Column(Integer, nullable=False)
    payment_currency = Column(String(50), nullable=True)



