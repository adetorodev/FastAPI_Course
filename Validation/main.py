from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()  # Create an instance of FastAPI

@app.get("/")  # Define a GET endpoint
def read_root():
    return {"message": "Hello, World!"}

# String Validation
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
def validate_string(name: str = Query(..., min_length=3, max_length=50)):
    # The "..." indicates that this parameter is required.
    return {"name": name}

# Number Validation

@app.get("/items_b")
def validate_number(age: int = Query(..., gt=0, lt=120)):
    # The parameter must be between 1 and 119.
    return {"age": age}

# Number validations: greater than or equal

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)],
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results