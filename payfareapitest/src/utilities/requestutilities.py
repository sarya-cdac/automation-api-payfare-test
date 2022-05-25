from payfareapitest.src.configs.hosts_config import *
import logging as logger
import requests
import os
import json
from payfareapitest.src.resources.apiresources import *


class RequestUtility(object):

    def __init__(self):
        self.rs_json = None
        self.expected_status_code = None
        self.status_code = None
        self.url = None
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.get_bookend_point = ApiResources.getBook

    def get(self, endpoint, params, headers=None, expected_status_code=200):
        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, params={'AuthorName': 'Rahul Shetty'})
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        assert self.status_code == self.expected_status_code, "Verified"
        self.rs_json = rs_api.json()
        logger.debug(f"GET API response: {self.rs_json}")
        return self.rs_json

    def post(self, endpoint, payload, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers)
        self.status_code = rs_api.status_code
        print("The actual status code is ", self.status_code)
        print("The expected status code is", expected_status_code)
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        assert self.rs_json['Msg'] == 'successfully added'
        assert self.status_code == self.expected_status_code, "Verified"
        logger.debug(f"POST API response: {self.rs_json}")
        return self.rs_json
