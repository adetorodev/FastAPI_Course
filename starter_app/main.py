from fastapi import FastAPI

app = FastAPI()  # Create an instance of FastAPI

# @app.get("/")  # Define a GET endpoint
# def read_root():
#     return {"message": "Hello, World!"}


# Path parameters are a way to include dynamic values in the
# URL's path, allowing you to create RESTful APIs that respond
# based on the values provided in the path

# Defining Path Parameters
# Type Validation
# Order of Parameters

items = {
    1: {"name": "Laptop", "price": 1000, "order_id": 4},
    2: {"name": "Phone", "price": 500, "order_id": 4},
    3: {"name": "Tablet", "price": 300, "order_id": 4}
}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return items[item_id]

@app.get("/item/{item_id}/orders/{order_id}")
async def get_order(item_id: int, order_id: int):
    return {
        "item_id": item_id,
        "order_id": order_id,
        "status": "processing"
    }


@app.get("/users/me")
async def read_user_me():
    return {"user": "current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}