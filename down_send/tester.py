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


# ip_proxy0 = '193.43.119.41'
# ip_proxy1 = '193.43.119.3'
# ip_proxy2 = '5.188.183.221'
# ip_proxy3 = '5.188.181.86'



# proxy_list = ['193.43.119.41',
#               '193.43.119.3',
#               '5.188.183.221',
#               '5.188.181.86']
# # BUG in URLLIB YOU HAVE TO DOWNGRADE URLLIB:  pip install urllib3==1.25.8
# port = '34512'
# user = 'vadymkozak3S7'
# password = 'D9m2IkU'

# session = HTMLSession()
# for proxy_ip in proxy_list:
#     #proxy = 'http://username:password@ip:port'
#     proxy = 'https://'+ user +':'+ password +'@'+ proxy_ip +':'+ port
#     r = session.get(url, proxies={ 'http':proxy })#proxies={ 'http':proxy,'https':proxy})

l = ['a', 2 , 2]

for n in l:
    try:
        n + 1
    except TypeError as e:
        print('n1')
    except Exception as e:
        print('n2')
        print(e)
        print(Exception.traceback)
