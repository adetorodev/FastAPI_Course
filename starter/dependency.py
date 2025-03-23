from typing import Annotated

from sqlmodel import Session, SQLModel
from .dbConn import engine

async def create_db_and_table():
    print("DB Created")
    SQLModel.metadata.create_all(engine)

def get_session():
    with session(engine) as session:
        yield session

