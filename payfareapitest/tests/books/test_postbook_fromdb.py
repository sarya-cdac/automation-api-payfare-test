import pytest

from payfareapitest.src.utilities.generic import *
from payfareapitest.src.utilities.requestutilities import *
from payfareapitest.src.helpers.books_helpers import *
from payfareapitest.src.dao.books_dao import booksDAO


@pytest.mark.tcid31
def test_post_book_details_fromDB():
    logger.info("This is a post request for pytest for DB")

    book_obj_from_db = BooksHelper()
    rs_json_book_db = book_obj_from_db.create_book_from_db_query()
    print(rs_json_book_db)
