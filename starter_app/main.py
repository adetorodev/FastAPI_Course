from fastapi import FastAPI

app = FastAPI()  # Create an instance of FastAPI

# @app.get("/")  # Define a GET endpoint
# def read_root():
#     return {"message": "Hello, World!"}


# Query parameters are used to send additional data to the API without including it in the URL path. They are
# appended to the URL after a ? and are separated by & for multiple parameters

# Optional by Default
# Validation with Type Hints
# Default Values
# Automatic Documentation