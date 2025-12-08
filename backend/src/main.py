from contextlib import asynccontextmanager
import os

from fastapi import FastAPI
from api.chat.routing import router as chat_router

from api.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs on startup
    init_db()
    yield
    # This runs on shutdown

app = FastAPI(lifespan=lifespan)

app.include_router(chat_router)

@app.get("/")
def read_root():
    return {"Hello": "World gouds 566"}