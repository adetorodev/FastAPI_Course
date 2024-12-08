from fastapi import FastAPI

app = FastAPI()  # Create an instance of FastAPI

@app.get("/")  # Define a GET endpoint
def read_root():
    return {"message": "Hello, World!"}


# http://127.0.0.1:8000/docs#/default/read_root__get
# http://127.0.0.1:8000/openapi.json
# http://127.0.0.1:8000/