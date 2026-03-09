from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Allow browser requests from file:// and localhost (needed for the Python Bootcamp simulator)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Book(BaseModel):
    title: str
    price: float
    category: str

books_db = [
    {"id": 1, "title": "Clean Code", "price": 29.99, "category": "tech"},
    {"id": 2, "title": "Dune", "price": 14.99, "category": "sci-fi"},
    {"id": 3, "title": "The Pragmatic Programmer", "price": 34.99, "category": "tech"},
]

@app.get("/")
def root():
    return {"message": "Book Store API", "total": len(books_db)}

@app.get("/books")
def get_books(category: Optional[str] = None):
    if category:
        return [b for b in books_db if b["category"] == category]
    return books_db

@app.post("/books", status_code=201)
def create_book(book: Book):
    new_book = {"id": len(books_db) + 1, **book.dict()}
    books_db.append(new_book)
    return new_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    book = next((b for b in books_db if b["id"] == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    books_db.remove(book)
    return {"deleted": book_id}
