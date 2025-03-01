

from fastapi import FastAPI, Depends, HTTPException, APIRouter, BackgroundTasks, Query
from typing import Optional

app = FastAPI()




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



