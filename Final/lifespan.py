from fastapi import FastAPI
from depedency import create_db_and_tables, get_session

def create_start_app_handler(app: FastAPI) -> callable:
    async def start_app() -> None:
        await create_db_and_tables()
        await get_session()
    return start_app

# def create_stop_app_handler(app: FastAPI) -> callable:
#     async def stop_app() -> None:
#         await close_mongo_connection()
#     return stop_app