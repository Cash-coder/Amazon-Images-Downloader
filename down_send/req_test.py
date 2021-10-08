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
import json
import shutil
import logging


def save_html_response(r, item='-'):
    item = item.replace(' ', '_')
    with open(item + 'response.html','w',encoding='utf-8') as f:
        f.write(r.text)

session = HTMLSession()
headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

url = 'https://www.backmarket.es/sony-sony-xperia-1-128-gb-negro-libre-segunda-mano/336533.html#l=12'

r = session.get(url, headers=headers, allow_redirects=True)#, proxies={ 'http':proxy })#proxies={ 'http':proxy,'https':proxy})

tags = r.html.xpath('//div[@class="flex justify-center md:hidden"]/div/div/ul/li/img')
search_pattern = r'https(.*?).jpg'
for tag in tags:
    # print(tag)
    url = re.search(search_pattern, str(tag))
    # print(url)
    if url != None:
        print(url.group())
    else: print('no match')



# tag = ''' Element 'img' height='560' width='560' alt='Sony Xperia 1' decoding='async' loading='lazy' sizes='100vw' src='/cdn-cgi/image/format=auto,quality=75,width=640/https://d1eh9yux7w8iql.cloudfront.net/product_images/1584612768.9552991.jpg' srcset='/cdn-cgi/image/format=auto,quality=75,width=640/https://d1eh9yux7w8iql.cloudfront.net/product_images/1584612768.9552991.jpg 640w,/cdn-cgi/image/format=auto,quality=75,width=750/https://d1eh9yux7w8iql.cloudfront.net/product_images/1584612768.9552991.jpg 750w,/cdn-cgi/image/format=auto,quality=75,width=828/https://d1eh9yux7w8iql.cloudfront.net/product_images/1584612768.9552991.jpg 828w,/cdn-cgi/image/format=auto,quality=75,width=1080/https://d1eh9yux7w8iql.cloudfront.net/product_images/1584612768.9552991.jpg 1080w,/cdn-cgi/image/format=auto,quality=75,width=1200/https://d1eh9yux7w8iql.cloudfront.net/product_images/1584612768.9552991.jpg 1200w,/cdn-cgi/image/format=auto,quality=75,width=1920/https://d1eh9yux7w8iql.cloudfront.net/product_images/1584612768.9552991.jpg 1920w,/cdn-cgi/image/format=auto,quality=75,width=2048/https://d1eh9yux7w8iql.cloudfront.net/product_images/1584612768.9552991.jpg 2048w,/cdn-cgi/image/format=auto,quality=75,width=3840/https://d1eh9yux7w8iql.cloudfront.net/product_images/1584612768.9552991.jpg 3840w' class=('mt-3', 'block', 'wrAXteFB', '_3UliecWHPgGxJvw6AgnixG')>'''
# search_data = r'https(.*?).jpg'
# url = re.search(search_data, tag)
# print(url)
# print(url.group())

# #findall(r'hiRes(.*?).jpg', s)