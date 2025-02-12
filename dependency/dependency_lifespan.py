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

# Using Lifespan Dependencies
@asynccontextmanager
async def lifespan_dependency():
    # Create resource (e.g., database connection) at startup
    resource = "Connected to DB"
    print("Resource Created")
    yield resource
    # Clean up resource at shutdown
    print("Resource Destroyed")

@app.get("/resource")
async def get_resource(resource: str = Depends(lifespan_dependency)):
    return {"resource": resource}

# Combining Scopes

# Application-scoped dependency
class DatabaseConnection:
    def __init__(self):
        self.connection = "Connected to Database"

    def __call__(self):
        return self.connection

db_connection = DatabaseConnection()

# Request-scoped dependency
def get_current_user(token: str):
    # Simulate token validation
    if token != "valid-token":
        raise ValueError("Invalid token")
    return {"username": "john_doe"}

@app.get("/data")
def get_data(
    user: dict = Depends(get_current_user),
    db: str = Depends(db_connection)
):
    return {
        "user": user,
        "db": db
    }

# Dependency Scopes for Testing
class DatabaseConnection:
    def __init__(self):
        self.connection = "Connected to Database"

    def __call__(self):
        return self.connection

db_connection = DatabaseConnection()

@app.get("/data")
def get_data(db: str = Depends(db_connection)):
    return {"db": db}

# Test client with dependency override
def test_get_data():
    def mock_db_connection():
        return "Mocked Database Connection"

    app.dependency_overrides[db_connection] = mock_db_connection

    client = TestClient(app)
    response = client.get("/data")
    assert response.json() == {"db": "Mocked Database Connection"}