from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author, BookOut

from typing import List

app = FastAPI()

@app.post('/book')
def create_book(item: Book, author: Author, quantity: int = Body(...)):
    return {'item': item, 'author': author, 'quantity': quantity}


# @app.get('/book')
# def get_book(q: str = Query(None, min_length=2, max_length=10, description='Search book')):
#     return q


@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int=Query(None, gt=10, le=500)):
    return {'pk': pk, 'pages': pages}


@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    return {'author': author}


@app.post('/books', response_model=Book, response_model_include={"pages", "date"})
def create_book(item: Book):
    return item


@app.post('/Bookout', response_model=BookOut)
def create_bookout(item: Book):
    return BookOut(**item.dict(), id=3)









