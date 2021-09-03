from requests_html import HTMLSession

from re import sub
from decimal import Decimal

#n = '1.211,91'
#money = '$6,150,593.22'
#value = Decimal(sub(r'[^\d.]', '', n))


# print(type(value))
# print(value)

t = ['1.211,91','659,00','85,99']

for price in t:
    print('input',price)
    price = price.split(',')[0]
    if '.' in price:
        n = price.replace('.',',')
        price = Decimal(sub(r'[^\d.]', '', n))
        price = int(price)
        print('output1: ',price)
        print(type(price))
    else:
        price = Decimal(sub(r'[^\d.]', '', price))
        print('output:2 ',price)
        price = int(price)
        print(type(price))



    # if len(price) > 3:
    #     price = price.replace('.',',')
    # else:
    #     price = int(price)


# headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"} 

# session = HTMLSession()

# url = 'https://www.amazon.es/s?k=iphone+xr+amarillo&i=electronics&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2'

# r = session.get(url,headers=headers,allow_redirects=True) 

# prods = r.html.xpath('//div[@data-component-type="s-search-result"]')

# for p in prods:
#     title= p.xpath('//div[@class="a-section a-spacing-none a-spacing-top-small"]/h2')[0].text
#     price = p.xpath('//span[@class="a-price-whole"]')[0].text
#     print(title)
#     print(price)



# # if title in splitted and attribute_p in title:
# #     #if prod.text not in ['Carcasa', 'Funda', 'Protector', 'Soporte'] :
# #     #if 'Carcasa' and 'Funda' and 'Protector' and 'Soporte' not in prod.text:
# #     if 'carcasa' not in title and 'funda' not in title and 'protector' not in title and 'soporte' not in title:
# #         print('match')
# # else:
# #     print('not found:')
# #     print(r"\n")