#https://pypi.org/project/mega.py/
from csv import excel
from mega import Mega
import login_file # .py file with MEGA user and password
from requests_html import HTMLSession
import requests
import re
from time import sleep
from openpyxl import load_workbook
from openpyxl.workbook.workbook import Workbook
import os
import traceback
import login_file # .py file with MEGA user and password
import logging

from logging import getLoggerClass, addLevelName, setLoggerClass, NOTSET

VERBOSE = 5

class MyLogger(getLoggerClass()):
    def __init__(self, name, level=NOTSET):
        super().__init__(name, level)

        addLevelName(VERBOSE, "VERBOSE")

    def verbose(self, msg, *args, **kwargs):
        if self.isEnabledFor(VERBOSE):
            self._log(VERBOSE, msg, args, **kwargs)

setLoggerClass(MyLogger)

logging.Logger.Mylogger('is this working?')

# DEBUG_LEVELV_NUM = 9 
# logging.addLevelName(DEBUG_LEVELV_NUM, "MYLOG")
# logging.basicConfig(level=logging.MYLOG)

# logging.mylog('got mega credentials')


# DEBUG_LEVELV_NUM = 9 
# logging.addLevelName(DEBUG_LEVELV_NUM, "DEBUGV")
# def debugv(self, message, *args, **kws):
#     # Yes, logger takes its '*args' as 'args'.
#     self._log(DEBUG_LEVELV_NUM, message, args, **kws) 
# logging.Logger.debugv = debugv

# logging.Logger('printed in screen and txt file')