from fastapi import FastAPI

app = FastAPI()  # Create an instance of FastAPI

@app.get("/")  # Define a GET endpoint
def read_root():
    return {"message": "Hello, World!"}

# Path Parameters

@app.get("/users/{user_id}")  # Path parameter defined in the route
def get_user(user_id: int):  # Type-hinted as an integer
    return {"user_id": user_id}

# Query Parameters
@app.get("/search")
def search_items(q: str = None, limit: int = 10):  # Default values can be provided
    return {"query": q, "limit": limit}

@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
