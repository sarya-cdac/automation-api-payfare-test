import os
import json
import logging as logger
from payfareapitest.src.utilities.requestutilities import RequestUtility
from payfareapitest.src.utilities.dbUtility import DBUtility
from payfareapitest.src.dao.books_dao import booksDAO


class BooksHelper(object):
    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.request_utility = RequestUtility()
        self.db_utility = DBUtility()
        self.body = None

    def create_book(self):
        payload_template = os.path.join(self.cur_file_dir, '..', 'data', 'payload.json')
        file_name = "C:\\Users\\Shivani Arya\\PycharmProjects\\AutomationPytest\\payfareapitest\\src\\data\\payload" \
                    ".json "
        with open(file_name) as f:
            payload = json.load(f)
        create_book_json = self.request_utility.post(endpoint='Library/Addbook.php', payload=payload,
                                                     expected_status_code=200)
        return create_book_json

    def create_book_from_db_query(self):

        # query_to_get_book_detail = books_dao_obj.get_books_details()
        sql = 'select * from books'
        logger.debug("This is a post request for pytest for DB")
        create_book_json_db = self.request_utility.post(endpoint='Library/Addbook.php',
                                                        payload=self.create_payload(sql),
                                                        expected_status_code=200)
        return create_book_json_db

    def create_payload(self, sql):
        addBody = {}
        tb = self.db_utility.execute_select(sql)
        addBody['name'] = tb[0]
        addBody['isbn'] = tb[1]
        addBody['aisle'] = tb[2]
        addBody['author'] = tb[3]
        return addBody
