import logging as logger
import pytest
from payfareapitest.src.utilities.generic import *
from payfareapitest.src.utilities.requestutilities import *
from payfareapitest.src.helpers.books_helpers import *
from payfareapitest.src.resources.apiresources import *


@pytest.mark.tcid29
@pytest.mark.smoke
def test_list_all_books():
    logger.info("This is a get request for pytest")
    req_helper = RequestUtility()
    rs_api = req_helper.get(endpoint=ApiResources.getBook, params={'AuthorName': 'Rahul Shetty'})
    print(rs_api)


@pytest.mark.tcid30
@pytest.mark.regression
def test_post_book_details():
    logger.info("This is a post request for pytest")
    book_obj = BooksHelper()

    book_payload_info = book_obj.create_book()
    print(book_payload_info)
