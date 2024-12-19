from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()  # Create an instance of FastAPI

# Request model definition
class UserRequest(BaseModel):
    username: str
    email: EmailStr
    age: int

class UserResponse(BaseModel):
    username: str
    age: int

@app.post("/register")
async def register_user(user: UserRequest):

    return {"message": "User registered successfully", "user": user}



@app.get("/user/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):

    return {"username": "johndoe", "age": 25}