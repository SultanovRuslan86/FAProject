from fastapi import FastAPI, Query
from schemas import Book

app = FastAPI()

@app.post('/book')
def create_book(item: Book):
    return item


@app.get('/book')
def get_book(q: str = Query(None, min_length=2, max_length=10, description='Search book')):
    return q














