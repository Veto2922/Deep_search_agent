from dotenv import load_dotenv
import os

import sqlmodel
from sqlmodel import Session , SQLModel

load_dotenv()

DATABASE_URL = os.getenv("POSTGRES_URL")

if DATABASE_URL is None or DATABASE_URL == "":
    raise ValueError("POSTGRES_URL is not set")

engine = sqlmodel.create_engine(DATABASE_URL)

def init_db():
    print("CREATING DATABASE TAbles")
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
