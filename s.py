from bs4 import BeautifulSoup as bs4
from requests_html import HTMLSession
import json
import pprint

url = 'https://www.amazon.es/Sennheiser-Auriculares-Bluetooth-Control-t%C3%A1ctil/dp/B08CZQXLQJ/ref=dp_prsubs_2?pd_rd_i=B08CZQXLQJ&psc=1'

headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
session = HTMLSession()

r = session.get(url,headers=headers)
status = r.status_code

if status == 200:

    with open('resuls.txt','w',encoding='utf-8') as f:
        f.write(r.text)

    #soup = bs4(r.text, 'lxml')
    soup = bs4(r.content, 'lxml')

    #tag = soup.xpath('//div[@id="twister-main-image"]')
    #tag = r.html.xpath('//div[@class="collections-collect-button"]')
    tag = r.html.find('script', containing='P.when(\'A\').register("ImageBlockATF", function(A){')
    #tag = str(tag)

    #tag = soup.xpath('//div[@id="twister-main-image"]//preceding-sibling::script')
    #print(tag.absolute_links)
    
    for e in tag:
        print(e.text)
    #     my_json = json.loads(e.text)
    # print(my_json)
    
else:
    print("Response status:{}".format(status))

'''
    P.when('A').register("ImageBlockATF", function(A){
'''