from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    name: str
    id: int

books = []

@app.get("/read_books")
async def read_books():
    return books


@app.post("/add_book")
async def add_book(b: Book):
    data = {"id": b.id, "name": b.name}
    books.append(data)
    return {"message": "New book is added successfully"}


@app.put("/update_book/{id}")
async def update_book(id: int, b: Book):
    for book in books:
        if book["id"] == id:
            book["name"] = b.name
            return {"message": "Book is updated successfully"}
    return {"message": "Book is not found"}

@app.delete("/delete_book/{id}")
async def delete_book(id: int):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return {"message": "Book is deleted successfully"}
    return {"message": "Book is not found"}
