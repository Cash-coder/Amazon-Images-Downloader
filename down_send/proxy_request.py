https://pypi.org/project/mega.py/
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

def proxy_request(url):

    proxy_list = ['193.43.119.41',
                '193.43.119.3',
                '5.188.183.221',
                '5.188.181.86']

    # BUG in URLLIB YOU HAVE TO DOWNGRADE URLLIB:  pip install urllib3==1.25.8
    port = '34512'
    user = 'vadymkozak3S7'
    password = 'D9m2IkU'
    target_url = 'http://www.whatismyproxy.com/'

    session = HTMLSession()
    for proxy_ip in proxy_list:
        #proxy = 'http://username:password@ip:port'
        proxy = 'https://'+ user +':'+ password +'@'+ proxy_ip +':'+ port
        r = session.get(target_url, proxies={ 'http':proxy })#proxies={ 'http':proxy,'https':proxy})


#################################################################

proxy_error_count_0 = 0
proxy_error_count_1 = 0
proxy_error_count_2 = 0
proxy_error_count_3 = 0
def proxy_request(url,item):
    ''' url, item // Version 2, pops out proxies with +100 accumulated errors'''
    global proxy_error_count_0 
    global proxy_error_count_1 
    global proxy_error_count_2 
    global proxy_error_count_3 
    '''url // downgrade urlib'''
    
    proxy_list = ['193.43.119.41',
              '193.43.119.3',
              '5.188.183.221',
              '5.188.181.86']
    
    # BUG in URLLIB YOU HAVE TO DOWNGRADE URLLIB:  pip install urllib3==1.25.8
    port = '34512'
    user = 'vadymkozak3S7'
    password = 'D9m2IkU'

    session = HTMLSession()
    headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
    
    #Try with proxies, if error try another and add error to list, if errors list > 100, pop() that proxy
    retries = 0
    n_proxys = len(proxy_list)
    while retries < n_proxys:
        try:
            #proxy = 'http://username:password@ip:port'
            proxy = 'https://'+ user +':'+ password +'@'+ proxy_list[retries] +':'+ port
            r = session.get(url,headers=headers, allow_redirects=True, proxies={ 'http':proxy })#proxies={ 'http':proxy,'https':proxy})
            status = r.status_code
            
            if status == 200:
                return r #this breaks the loop
                 
            #All proxies tested without 200 code
            elif status != 200 and retries == n_proxys:
                print(f'ALL proxies tested, any 200 code, status: {status}, item: {item}, URL: {url}') 
                #write_bad_result(url=url,item=item)
                return 'request error'
            #still proxy left to retry:
            elif status != 200:
                print(f'error proxy, status: {status}, proxy: {proxy_list[retries]}, URL: {url}') 
                retries += 1
                
                #to maintain only healthy proxies 
                if   retries == 0: proxy_error_count_0 += 1
                elif retries == 1: proxy_error_count_1 += 1
                elif retries == 2: proxy_error_count_2 += 1
                elif retries == 3: proxy_error_count_3 += 1

                if   proxy_error_count_0 > 100: proxy_list.pop(0)
                elif proxy_error_count_1 > 100: proxy_list.pop(1)
                elif proxy_error_count_2 > 100: proxy_list.pop(2)
                elif proxy_error_count_3 > 100: proxy_list.pop(3)
            
        except Exception as e:
            print(e)
            pass

######################################################


