from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from typing import List
from pydantic import BaseModel
from .model import User, UpdateUser


@asynccontextmanager
async def lifespan(app: FastAPI):
    await start_db_client(app)
    yield

    await shutdown_db_client(app)

async def start_db_client(app):
    app.mongodb_Client = AsyncIOMotorClient(
        "mongodb://localhost:27017/"
    )
    app.mongodb = app.mongodb_Client.get_database("collegeDB")

    print("MongoDb connected")


async def shutdown_db_client(app):
    app.mongodb_client.close()
    print("Database disconnected")

app = FastAPI(lifespan=lifespan)


user_collection = app.mongodb['users']
@app.post("/users", response_model= User)
async def insert_user(user: User):
    result = await user_collection.insert_one(user.model_dump())
    inserted_user = await user_collection.find_one({"_id": result.inserted_id})
    return inserted_user

@app.get("/users", response_model=List[User])
async def reas_user():
    users = await user_collection.find().to_list(None)
    return users

@app.get("/users/{email_address}", response_model=User)
async def read_user_email(email_address: str):
    user = await user_collection.find_one({"email_address": email_address})
    if user is None:
        raise HTTPException(status_code =404, detail="user not found")
    return user

@app.put("/user/{email_address}", response_model = User)
async def update_user(email_address: str, user_update: UpdateUser):
    updated_result = await user_collection.update_one(
        {"email_address": email_address},{
            "$set": user_update.model_dump(exclude_unset=True)
        }
    )
    if updated_result.modified_count ==0:
        raise HTTPException(status_code =404, detail="user not found")
    updated_usr = await user_collection.find_one({"email_address": email_address})
    return updated_usr


@app.delete("/user/{email_address}", response_model = dict)
async def delete_user(email_address: str):
    deleted_result = await user_collection.delete_one(
        {"email_address": email_address}
    )
    if deleted_result.deleted_count ==0:
        raise HTTPException(status_code =404, detail="user not found")
    return {"message": "user deleted successfully"}

