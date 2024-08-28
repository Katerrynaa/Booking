from fastapi import FastAPI
from src.views import router
import uvicorn


app = FastAPI()
app.include_router(router)

if __name__ == "__main__":  
    uvicorn.run("main:app", port=8000, log_level="info")