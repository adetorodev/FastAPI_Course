

from fastapi import FastAPI, Depends, HTTPException, APIRouter, BackgroundTasks, Query
from typing import Optional

app = FastAPI()


# Define a dependency
def get_current_user():
    return {"user_id": 1, "username": "john_doe"}

# Inject the dependency into the endpoint
@app.get("/profile")
def read_profile(current_user: dict = Depends(get_current_user)):
    return {"user": current_user}

# Injecting Nested Dependencies
# Another dependency that depends on `get_user`
def get_user_details(user: dict = Depends(get_current_user)):
    return {"user_id": user["user_id"], "email": "john_doe@example.com"}

# Endpoint using the nested dependency
@app.get("/details")
def user_details(details: dict = Depends(get_user_details)):
    return details


# Using Dependencies with Default and Optional Values
# Dependency with a default value
def get_message(msg: str = "Hello, World!"):
    return msg

@app.get("/message")
def read_message(message: str = Depends(get_message)):
    return {"message": message}

# Injecting Dependencies at the Global Level
# Define a global dependency
def verify_token(token: str = "default-token"):
    if token != "default-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

# Add the dependency globally
@app.middleware("http")
async def add_global_dependency(request, call_next):
    # Example of globally injecting verify_token logic
    request.state.token = verify_token()
    response = await call_next(request)
    return response

@app.get("/endpoint")
def endpoint():
    return {"message": "Token verified"}


# Group-Level Dependencies
# Dependency for verifying an API key
router = APIRouter()
def verify_api_key(api_key: str):
    if api_key != "valid-key":
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return api_key

# Add the dependency to a router
@router.get("/secure-data", dependencies=[Depends(verify_api_key)])
def secure_data():
    return {"data": "This is secure"}

app.include_router(router, prefix="/api")

# Injecting Dependencies with Classes
# Dependency as a class
class DatabaseConnection:
    def __init__(self):
        self.connection = "Database Connected"

    def __call__(self):
        return self.connection

# Inject the class dependency
@app.get("/db-status")
def db_status(db: str = Depends(DatabaseConnection())):
    return {"status": db}

# Injecting Dependencies in Background Tasks
# Dependency for a logger
def get_logger():
    def log(message: str):
        print(f"LOG: {message}")
    return log

# Background task using the logger dependency
def log_in_background(log: callable, message: str):
    log(message)

@app.post("/process")
def process(background_tasks: BackgroundTasks, log: callable = Depends(get_logger)):
    background_tasks.add_task(log_in_background, log, "Processing completed")
    return {"status": "Task running in background"}

# Injecting Dependencies for Authentication and Authorization
# Authentication dependency
def authenticate_user(token: str):
    if token != "valid-token":
        raise HTTPException(status_code=403, detail="Invalid or missing token")
    return {"user_id": 1, "username": "john_doe"}

@app.get("/protected")
def protected_route(user: dict = Depends(authenticate_user)):
    return {"message": f"Hello, {user['username']}!"}