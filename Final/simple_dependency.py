

from fastapi import FastAPI, Depends, HTTPException
from typing import Optional

app = FastAPI()

# def get_query_param(param: str = "default"):
#     return {"param": param}

# @app.get("/")
# async def get_root():
#     return {"message": "Welcome to FastAPI world!"}




# @app.get("/")
# def read_root(param: dict = Depends(get_query_param)):
#     return {"received_param": param}

#  How to Create a Simple Dependency
# Define a simple dependency
def get_message():
    return "Hello, this is a simple dependency!"

# Use the dependency in an endpoint
@app.get("/greet")
def greet(message: str = Depends(get_message)):
    return {"message": message}

# Using Default Values
# Define a dependency with default values
def get_message(message: str = "Default message"):
    return message

@app.get("/custom-greet")
def custom_greet(message: str = Depends(get_message)):
    return {"message": message}


# Passing Query Parameters to Dependencies
# Dependency that processes query parameters
def get_query_params(q: str = "default"):
    return {"query": q}

@app.get("/search")
def search(params: dict = Depends(get_query_params)):
    return {"search_result": params}


# Reusing Dependencies
# Reusable dependency
def get_user_info(user_id: int = 1):
    return {"user_id": user_id, "username": f"user{user_id}"}

@app.get("/user/profile")
def user_profile(user_info: dict = Depends(get_user_info)):
    return {"profile": user_info}

@app.get("/user/settings")
def user_settings(user_info: dict = Depends(get_user_info)):
    return {"settings": user_info}

# Combining Multiple Dependencies
# Define two simple dependencies
def get_user():
    return {"user_id": 1, "username": "john_doe"}

def get_settings():
    return {"theme": "dark", "notifications": True}

@app.get("/dashboard")
def dashboard(user: dict = Depends(get_user), settings: dict = Depends(get_settings)):
    return {"user": user, "settings": settings}

# Error Handling in Dependencies
# Dependency with input validation
def get_validated_user(user_id: int):
    if user_id < 1:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    return {"user_id": user_id, "username": f"user{user_id}"}

@app.get("/user/{user_id}")
def user_details(user: dict = Depends(get_validated_user)):
    return user