from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from fastapi.testclient import TestClient

app = FastAPI()

# Request-scoped dependency
def get_request_id():
    return "request-id"

@app.get("/process")
def process(request_id: str = Depends(get_request_id)):
    return {"request_id": request_id}

# Application-Level Dependencies (Application Scope)
# Application-scoped dependency
class AppState:
    def __init__(self):
        self.state = "Initialized"

    def __call__(self):
        return self.state

app_state = AppState()

@app.on_event("startup")
def startup_event():
    # Initialize shared resources
    app_state.state = "Application Started"

@app.on_event("shutdown")
def shutdown_event():
    # Clean up shared resources
    app_state.state = "Application Stopped"

@app.get("/app-state")
def get_app_state(state: str = Depends(app_state)):
    return {"state": state}