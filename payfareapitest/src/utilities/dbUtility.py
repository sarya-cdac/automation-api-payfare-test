import os

import mysql.connector
from mysql.connector import Error
from payfareapitest.src.utilities.credentialsUtility import CredentialsUtility
from payfareapitest.src.configs.hosts_config import *


class DBUtility(object):

    def __init__(self):
        creds_helper = CredentialsUtility()
        self.creds = creds_helper.get_db_credentials()
        self.host = db_hosts['machine1']['test']['host']
        self.database = db_hosts['machine1']['test']['database']
        self.username = db_hosts['machine1']['test']['username']
        self.password = db_hosts['machine1']['test']['password']

    def create_connection(self):
        conn = mysql.connector.connect(host=self.host, database=self.database,
                                       username=self.username, password=self.password)
        return conn

    def execute_select(self, sql):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        conn.close()
        return row

