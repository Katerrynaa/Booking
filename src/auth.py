import secrets
from typing import Annotated
import bcrypt

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from src.models import SessionLocal, User

app = FastAPI()

security = HTTPBasic()

def get_current_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)], 
):
    with SessionLocal() as session:
        user_credentials = session.query(User).filter(User.username == credentials.username).first()

        if user_credentials is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
        )

        if not bcrypt.checkpw(credentials.password.encode('utf-8'), user_credentials.password.encode('utf-8')):
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
        
        return credentials.username



