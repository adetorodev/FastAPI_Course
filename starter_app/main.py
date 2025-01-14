from fastapi import FastAPI, HTTPException, Query, Path
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

# In-memory data store
books_db = []

# Pydantic model for Book
class Book(BaseModel):
    id: int = Field(..., description="The unique ID of the book")
    title: str = Field(..., min_length=1, max_length=100, description="The title of the book")
    author: str = Field(..., min_length=1, max_length=50, description="The author of the book")
    price: float = Field(..., gt=0, description="The price of the book (must be greater than 0)")

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Learn FastAPI",
                "author": "John Doe",
                "price": 19.99
            }
        }

@app.get("/books", response_model=List[Book])
def list_books(title: Optional[str] = Query(None, description="Filter books by title")):
    """
    List all books. Optionally filter books by title using a query parameter.
    """
    if title:
        filtered_books = [book for book in books_db if title.lower() in book["title"].lower()]
        return filtered_books
    return books_db

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int = Path(..., description="The ID of the book to retrieve")):
    """
    Get a book by its ID.
    """
    for book in books_db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book)
def add_book(book: Book):
    """
    Add a new book to the collection. Validates input data.
    """
    for existing_book in books_db:
        if existing_book["id"] == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")
    books_db.append(book.dict())
    return book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    """
    Update a book by its ID. Validates input data.
    """
    for idx, book in enumerate(books_db):
        if book["id"] == book_id:
            books_db[idx] = updated_book.dict()
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int = Path(..., description="The ID of the book to delete")):
    """
    Delete a book by its ID.
    """
    for idx, book in enumerate(books_db):
        if book["id"] == book_id:
            books_db.pop(idx)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
