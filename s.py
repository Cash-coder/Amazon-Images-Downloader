from bs4 import BeautifulSoup as bs4
import requests
url = 'https://www.amazon.es/Sennheiser-Auriculares-Bluetooth-Control-t%C3%A1ctil/dp/B08CZQXLQJ/ref=dp_prsubs_2?pd_rd_i=B08CZQXLQJ&psc=1'
headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

r = requests.get(url,headers=headers)
status = r.status_code
print(status)

if status == 200:

    with open('resuls.txt','w',encoding='utf-8') as f:
        f.write(r.text)

    soup = bs4(r.text, 'lxml')
    #soup = bs4(r.content, 'lxml')

    tag = soup.xpath('//div[@id="twister-main-image"]')
    #tag = soup.xpath('//div[@id="twister-main-image"]//preceding-sibling::script')
    print(tag)
    #pics = soup.find_all('script')#:"text/javascript")
    #for pic in pics:
        #print(len(pic))

    #for tag in soup.find_all('script'):#:"text/javascript")
        #print(len(e.text))
        #print(len(soup.find(e.name).text))

    #print(len(pics))
    '''
    P.when('A').register("ImageBlockATF", function(A){
    '''
else:
    print("Response status:{}".format(status))