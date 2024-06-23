import string
import sys

import requests

import connectionController


def assert_status_code(response: requests.Response, status_code: int):
    assert response.status_code == status_code


def assert_ret_value(response: requests.Response, returned_value: any):
    assert response.json() == returned_value


def assert_valid_added_resource(response: requests.Response):
    assert response.status_code == 201
    # should be positive ID
    VALID_RETURNED_RESOURCE_ID = 0
    print("print(response.json()) > 0? response.json() =")
    print(response.json())
    sys.stdout.flush()
    assert response.json() > VALID_RETURNED_RESOURCE_ID


def assert_not_existed_book(book_identifier: any) -> None:
    response = connectionController.http_get(f"books/{book_identifier}")
    assert_status_code(response, 404)
    assert_ret_value(response, 5)
