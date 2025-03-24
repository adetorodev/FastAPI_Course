from fastapi import FastAPI
from .dependency import create_db_and_table, get_session
from contextlib import asynccontextmanager


@asynccontextmanager
async def create_start_app_handler(app: FastAPI):
    await create_db_and_table()
    # get_session()
    yield()