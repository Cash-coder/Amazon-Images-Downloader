from bs4 import BeautifulSoup as bs4
from requests_html import HTMLSession
import re
import json
import pprint

url = 'https://www.amazon.es/Sennheiser-Auriculares-Bluetooth-Control-t%C3%A1ctil/dp/B08CZQXLQJ/ref=dp_prsubs_2?pd_rd_i=B08CZQXLQJ&psc=1'

headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
session = HTMLSession()

r = session.get(url,headers=headers)
status = r.status_code

if status == 200:

    with open('result.html','w',encoding='utf-8') as f:
        f.write(r.text)

    #soup = bs4(r.text, 'lxml')
    #soup = bs4(r.content, 'lxml')

    tag = r.html.find('script', containing='P.when(\'A\').register("ImageBlockATF", function(A){')
    #soup = bs4(tag[0].text,'lxml')
    s = tag[0].text
    #print(s)
    print(type(s))
    
    #pattern = re.compile(r'\.jpg$')#^hiRes
    #pattern2 = re.compile(r'?:http\:|https\:)?\/\/.*\.(?:png|jpg')#^hiRes
    #matches = pattern2.finditer(s)
    #matches = re.findall(r'^[hiRes]',s)
    matches = re.findall(r'hiRes',s)
    for match in matches:
        print(match)
    
else:
    print("Response status:{}".format(status))

'''
    P.when('A').register("ImageBlockATF", function(A){
'''