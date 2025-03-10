from sqlmodel import create_engine
from typing import Annotated

db_name = "database.db"
sqlite_url = f"sqlite:///{db_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)