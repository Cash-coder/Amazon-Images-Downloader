from bs4 import BeautifulSoup as bs4
from requests_html import HTMLSession
import re
import json
import pprint

url = 'https://www.amazon.es/Apple-iPhone-64GB-Plata-Reacondicionado/dp/B082DKM8TG/ref=sr_1_3?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3L65HJLXS1PD9&dchild=1&keywords=iphine11&qid=1630505792&s=electronics&sprefix=iphi%2Celectronics%2C185&sr=1-3'

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
    
    # hiRes == High Resolution 
    # main  ==  ?
    #large  == 
    matches = re.findall(r'large(.*?).jpg',s)
    for match in matches:
        if '{' in match:
            url = match.replace('":{"','') + '.jpg'
        else:
            url = match.replace('":"','') + '.jpg'

        print(url)
    
    
else:
    print("Response status:{}".format(status))

'''
    P.when('A').register("ImageBlockATF", function(A){
'''