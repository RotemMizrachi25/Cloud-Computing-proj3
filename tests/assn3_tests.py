import pytest
import connectionController as cc
from assertions import *

# Test data
book1 = {"title": "Adventures of Huckleberry Finn", "ISBN": "9780520343641", "genre": "Fiction"}
book2 = {"title": "The Best of Isaac Asimov", "ISBN": "9780385050784", "genre": "Science Fiction"}
book3 = {"title": "Fear No Evil", "ISBN": "9780394558783", "genre": "Biography"}
book4 = {"title": "No such book", "ISBN": "0000001111111", "genre": "Biography"}
book5 = {"title": "The Greatest Joke Book Ever", "authors": "Mel Greene", "ISBN": "9780380798490", "genre": "Jokes"}
Book6 = {"title": "The Adventures of Tom Sawyer", "ISBN": "9780195810400", "genre": "Fiction"}
book7 = {"title": "I, Robot", "ISBN": "9780553294385", "genre": "Science Fiction"}
book8 = {"title": "Second Foundation", "ISBN": "9780553293364", "genre": "Science Fiction"}

book_ids = {}

def test_post_books():
    books = [book1, book2, book3]
    ids = set()

    for book in books:
        response = cc.http_post('books', book)
        assert response.status_code == 201
        book_id = response.json()['id']
        assert book_id not in ids
        ids.add(book_id)
        book_ids[book['title']] = book_id


def test_get_book1_by_id():
    book_id = book_ids.get("Adventures of Huckleberry Finn1")
    response = cc.http_get(f'books/{book_id}')
    assert response.status_code == 200
    assert response.json()['authors'] == "Mark Twain"


def test_get_all_books():
    response = cc.http_get("books")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_post_book4():
    response = cc.http_post('books', book4)
    assert response.status_code == 500


def test_delete_book2():
    book_id = book_ids.get("The Best of Isaac Asimov")
    response = cc.http_delete(f'books/{book_id}')
    assert response.status_code == 200


def test_get_deleted_book2_by_id():
    book_id = book_ids.get("The Best of Isaac Asimov")
    response = cc.http_get(f'books/{book_id}')
    assert response.status_code == 404


def test_post_book5():
    response = cc.http_post('books', book5)
    assert response.status_code == 422

