import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app import models
from app.api.api_v1.api import api_router
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_headers=['*'],
    allow_methods=['*'],
    allow_origins=['*'],
)
app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
