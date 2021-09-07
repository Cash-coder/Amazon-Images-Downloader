from twocaptcha import TwoCaptcha
from decimal import Decimal
from re import sub
from time import sleep

from bs4 import BeautifulSoup as bs4
from requests_html import HTMLSession
import re
import traceback

import xlsxwriter
from openpyxl.workbook.workbook import Workbook
from openpyxl import load_workbook


import undetected_chromedriver.v2 as uc
options = uc.ChromeOptions() 
#options.add_argument('--headless') 
#options.add_argument('--disable-gpu') 
d = uc.Chrome(options=options)

#with d:
d.get('')


# #####################
# def save_response(r):
#     global nr
#     with open('response.html','wb') as f:
#         f.write(r.content)
#     print('saved response')

# headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
# session = HTMLSession()

# url = 'https://www.pccomponentes.com/apple-iphone-xr-128gb-amarillo-libre-refurbished'
# r = session.get(url,headers=headers,allow_redirects=True)#proxies=proxies,)
# print(r.status_code)

# save_response(r)

# pics  = r.html.xpath('//a[@class="fancybox"]/@href')

# for pic in pics:
#     print(pic.text)