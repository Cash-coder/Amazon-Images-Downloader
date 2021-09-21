from requests_html import HTMLSession
import requests

url = 'https://www.backmarket.es/iphone-xs-max-64-gb-gris-espacial-libre-segunda-mano/166063.html?offer_type=6#l=11'

headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
session = HTMLSession()
r = session.get(url,headers=headers,allow_redirects=True)
    
tags = r.html.xpath('//div[@data-test="thumb-carousel"]/@style')
n = 0
for url in tags:
    url = url.replace('background-image:url(','').replace(');','').replace("'","")
    print(url)

    r = session.get(url)

    with open('pic'+ str(n) + '.jpg', 'wb') as f:
        f.write(r.content)
    n += 1




'div[@data-test="thumbs-bottom"]'
