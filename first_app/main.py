
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

class UpdatUser(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None

@app.get("/")
async def get_root():
    return {"message": "Welcome to FastAPI world!"}

@app.get("/users")
def get_user():
    return{"users" : ["Alice", "Bob", "John"]}

@app.post("/users")
def create_user(user: User):
    return {"message": f"User {user.name} created", "user": user}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Alice"}




@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {"message": f"user {user_id} updated", "user": user}

@app.patch("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {"message": f"User {user_id} partially updated", "updated_fields": user.dict(exclude_unset=True)}

@app.delete("/users/{user_id}")
def delete_user(user_id: int, user: UpdatUser):
    return {"message": f"user {user_id} deleted"}