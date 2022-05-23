import configparser
import logging as logger
from payfareapitest.src.configs.hosts_config import API_HOSTS
import os

'''Common function of read configurable files'''


def getConfig():
    config = configparser.ConfigParser()
    logger.debug("Reading config hosts file")
    config.read('../configs/hosts_config.py')
    return config



