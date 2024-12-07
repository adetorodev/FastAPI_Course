from fastapi import FastAPI

app = FastAPI()  # Create an instance of FastAPI

@app.get("/")  # Define a GET endpoint
def read_root():
    return {"message": "Hello, World!"}

# GET: Fetch data from the server.
# POST: Send data to create new resources.
# PUT: Update existing resources or create new ones if they don’t exist.
# DELETE: Remove resources from the server.

# An idempotent HTTP method is a method that can be invoked many times without different outcomes

@app.get("/items")  # Fetch a list of items
def get_items():
    return {"items": ["item1", "item2"]}

@app.post("/items")  # Create a new item
def create_item(item: str):
    return {"message": f"Item '{item}' created!"}

@app.put("/items/{item_id}")  # Update an item
def update_item(item_id: int, item: str):
    return {"message": f"Item '{item_id}' updated to '{item}'"}

@app.delete("/items/{item_id}")  # Delete an item
def delete_item(item_id: int):
    return {"message": f"Item '{item_id}' deleted!"}

