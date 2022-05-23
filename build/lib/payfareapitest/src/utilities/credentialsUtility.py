from payfareapitest.src.configs.hosts_config import *
import logging as logger
import os
import json


class CredentialsUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_db_credentials():
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')

        if not 'DB_USER' or not 'DB_PASSWORD':
            raise Exception('DB credentials must be present in env variables')
        else:
            return {'db_user': db_user, 'db_password': db_password}
