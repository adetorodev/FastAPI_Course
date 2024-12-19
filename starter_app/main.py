from fastapi import FastAPI
from typing import List, Optional
from fastapi import FastAPI, Query

app = FastAPI()  # Create an instance of FastAPI

@app.get("/validat-string")
async def validate_string(
     username: str = Query(
        ...,  # Indicates this parameter is required
        min_length=3,  # Minimum length of 3
        max_length=15,  # Maximum length of 15
        regex="^[a-zA-Z0-9_]+$",  # Allows only alphanumeric characters and underscores
        description="Username must be 3-15 characters long and can only contain letters, numbers, and underscores."
    )
):
    return {"message": f"Validate username: {username}"}

@app.get("/validat-number")
async def validate_number(
     age: int = Query(
        ...,  # Indicates this parameter is required
        ge=18,  # Minimum value (greater than or equal to 18)
        le=100,  # Maximum value (less than or equal to 100)
        description="Age must be between 18 and 100."
    )
):
    return {"message": f"Validated age: {age}"}

@app.get("/validate/")
async def validate(
    username: str = Query(..., min_length=3, max_length=15, regex="^[a-zA-Z0-9_]+$"),
    age: int = Query(..., ge=18, le=100)
):
    return {"message": f"Validated username: {username} and age: {age}"}

# Parameter	Type	Description
# min_length	String	Minimum length of a string.
# max_length	String	Maximum length of a string.
# regex	String	Regular expression pattern for a string.
# ge	Number	Greater than or equal to (minimum value).
# le	Number	Less than or equal to (maximum value).
# gt	Number	Greater than (exclusive minimum).
# lt	Number	Less than (exclusive maximum).