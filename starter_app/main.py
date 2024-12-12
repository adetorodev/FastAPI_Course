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
    1: {"name": "Laptop", "price": 1000},
    2: {"name": "Phone", "price": 500},
    3: {"name": "Tablet", "price": 300}
}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return items[item_id]