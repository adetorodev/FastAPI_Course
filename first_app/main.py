from fastapi import FastAPI

app = FastAPI()  # Create an instance of FastAPI

@app.get("/")  # Define a GET endpoint
def read_root():
    return {"message": "Hello, World!"}
