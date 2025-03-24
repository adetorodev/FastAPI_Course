# import fast api
from fastapi import FastAPI, HTTPException

# imports for the MongoDB database connection
from motor.motor_asyncio import AsyncIOMotorClient

# import for fast api lifespan
from contextlib import asynccontextmanager

from typing import List, Optional

from pydantic import BaseModel

from .model import User


# define a lifespan method for fastapi
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start the database connection
    await startup_db_client(app)
    yield
    # Close the database connection
    await shutdown_db_client(app)

# method for start the MongoDb Connection
async def startup_db_client(app):
    #
    app.mongodb_client = AsyncIOMotorClient(
        "mongodb+srv://ezadetoro:fastAPICourse_123@fastcourse.f5qgn.mongodb.net/?retryWrites=true&w=majority&appName=fastCourse")


    app.mongodb = app.mongodb_client.get_database("userbase")
    print("MongoDB connected.")

# method to close the database connection
async def shutdown_db_client(app):
    app.mongodb_client.close()
    print("Database disconnected.")

# creating a server with python FastAPI
app = FastAPI(lifespan=lifespan)

# hello world endpoint
@app.get("/")
def read_root():  # function that is binded with the endpoint
    return {"Hello": "World"}

# C <=== Create
@app.post("/api/v1/create-user", response_model=User)
async def insert_user(user: User):
    result = await app.mongodb["users"].insert_one(user.model_dump())
    inserted_user = await app.mongodb["users"].find_one({"_id": result.inserted_id})
    return inserted_user

# R <=== Read
# Read all users
@app.get("/api/v1/read-all-users", response_model=List[User])
async def read_users():
    users = await app.mongodb["users"].find().to_list(None)
    return users

# Read one user by email_address
@app.get("/api/v1/read-user/{email_address}", response_model=User)
async def read_user_by_email(email_address: str):
    user = await app.mongodb["users"].find_one({"email_address": email_address})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# U <=== Update
# Update user

class UpdateUserDTO(BaseModel):
    other_names: Optional[List[str]] = None
    age: Optional[int] = None
    # first_name: Optional[str] = None
    # last_name: Optional[str] = None
    # middle_name: Optional[str] = None
    # phone_number: Optional[str] = None

    class Config:
        extra = "forbid"

@app.put("/api/v1/update-user/{email_address}", response_model=User)
async def update_user(email_address: str, user_update: UpdateUserDTO):
    update_data = user_update.model_dump(exclude_unset=True)  # Only update provided fields

    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")

    updated_result = await app.mongodb["users"].update_one(
        {"email_address": email_address}, {"$set": update_data}
    )

    if updated_result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not found or no update needed")

    updated_user = await app.mongodb["users"].find_one({"email_address": email_address}, {"_id": 0})
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")

    return updated_user

# D <=== Delete
# Delete user by email_address
@app.delete("/api/v1/delete-user/{email_address}", response_model=dict)
async def delete_user_by_email(email_address: str):
    delete_result = await app.mongodb["users"].delete_one({"email_address": email_address})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}