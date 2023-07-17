from fastapi import FastAPI, Query, Path
from schemas import Book

from typing import List

app = FastAPI()

@app.post('/book')
def create_book(item: Book):
    return item


# @app.get('/book')
# def get_book(q: str = Query(None, min_length=2, max_length=10, description='Search book')):
#     return q


@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int=Query(None, gt=10, le=500)):
    return {'pk': pk, 'pages': pages}











