from bs4 import BeautifulSoup as bs4
from requests_html import HTMLSession
import requests
import re
import csv

def download_pictures(url): #To local machine
    n = 0
    pic = requests.get(url)
    file_name = 'Hi_Res_' + str(n) +'.jpg'
    n += 1
    
    with open(file_name, 'wb') as f:
        f.write(pic.content)

def save_html_response(r):
    with open('result.html','w',encoding='utf-8') as f:
        f.write(r.text)



'https://www.amazon.es/s?k=iphine+11+amarillo&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss'
url = 'https://www.amazon.es/Apple-iPhone-64GB-Plata-Reacondicionado/dp/B082DKM8TG/ref=sr_1_3?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3L65HJLXS1PD9&dchild=1&keywords=iphine11&qid=1630505792&s=electronics&sprefix=iphi%2Celectronics%2C185&sr=1-3'

headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
session = HTMLSession()

r = session.get(url,headers=headers,allow_redirects=True)
status = r.status_code

url_list = []
if status == 200:

    #save_html_response(r)

    #soup = bs4(r.text, 'lxml')
    #soup = bs4(r.content, 'lxml')
    #soup = bs4(tag[0].text,'lxml')

    tag = r.html.find('script', containing='P.when(\'A\').register("ImageBlockATF", function(A){')
    s = tag[0].text
    #print(s)
    
    # hiRes == High Resolution 
    # main  ==  ?
    # large ==  ?
    n = 1
    matches = re.findall(r'hiRes(.*?).jpg',s)
    print('LEN matches :',len(matches))
    for match in matches:
        if '{' in match:
            url = match.replace('":{"','') + '.jpg'
        else:
            url = match.replace('":"','') + '.jpg'
        print(url) 
        
        url_list.append(url)       
        #download_pictures(url)
    
    print(len(url_list))
    with open('URLs.csv','w') as f:
        fieldnames = ['Title','URL']
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        
        n = 0 #used to identify the picture 
        for item_url in url_list:
            title = 'query_test' + str(n)
            n +=1
            writer.writerow({'Title':title,'URL':item_url})


else:
    print("Response status:{}".format(status))

'''
    P.when('A').register("ImageBlockATF", function(A){
'''