

from fastapi import FastAPI, Depends, HTTPException, APIRouter, BackgroundTasks, Query
from typing import Optional

app = FastAPI()

# Using Classes as Dependencies in FastAPI

# Define a class-based dependency
class GreetingService:
    def __init__(self, name: str = "World"):
        self.name = name

    def __call__(self):
        return f"Hello, {self.name}!"

# Use the class as a dependency in an endpoint
@app.get("/greet")
def greet(service: str = Depends(GreetingService)):
    return {"message": service}

# Injecting Parameters into Class Dependencies
class GreetingService:
    def __init__(self, name: str):
        self.name = name

    def __call__(self):
        return f"Hello, {self.name}!"

# Dependency to extract the `name` parameter
def get_name(name: str = Query("World")):
    return name

@app.get("/personal-greet")
def personal_greet(service: str = Depends(lambda: GreetingService(get_name()))):
    return {"message": service}


# Managing State with Class Dependencies
class DatabaseService:
    def __init__(self):
        # Simulate a database connection
        self.connection = "Connected to database"

    def __call__(self):
        return self.connection

@app.get("/db-status")
def db_status(db_service: str = Depends(DatabaseService)):
    return {"status": db_service}

# Class Dependencies with Initialization Parameters
class UserService:
    def __init__(self, username: str):
        self.username = username

    def __call__(self):
        return f"User: {self.username}"

# Dependency to get the username
def get_username(username: str = Query("guest")):
    return username

@app.get("/user")
def user_info(user_service: str = Depends(lambda: UserService(get_username()))):
    return {"info": user_service}


# Using Class Dependencies with Subdependencies
# Dependency 1
def get_api_key():
    return "API-KEY-123"

# Class-based dependency that depends on get_api_key
class ApiKeyValidator:
    def __init__(self, api_key: str = Depends(get_api_key)):
        self.api_key = api_key

    def __call__(self):
        if self.api_key != "API-KEY-123":
            raise ValueError("Invalid API Key")
        return "API Key is valid"

@app.get("/validate-key")
def validate_key(api_key_status: str = Depends(ApiKeyValidator)):
    return {"status": api_key_status}


# Singleton Class Dependencies
class SingletonService:
    def __init__(self):
        self.state = "Initial State"

    def __call__(self):
        return self.state

# Create a single instance of the service
singleton_service = SingletonService()

@app.get("/singleton")
def get_state(service: str = Depends(lambda: singleton_service)):
    return {"state": service}