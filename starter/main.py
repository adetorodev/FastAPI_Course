from fastapi import FastAPI, Depends
from sqlmodel import Session, SQLModel
from database import engine
from typing import Annotated


app = FastAPI()  # Create an instance of FastAPI

def create_db_and_table():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SQLModel.metadata.create_all(engine)

SessionDep = Annotated[Session, Depends(get_session)]

@app.on_event("startup")
def on_startup():
    create_db_and_table()




