from requests_html import HTMLSession

headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"} 

session = HTMLSession()

url = 'https://www.amazon.es/s?k=iphone+xr+amarillo&i=electronics&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2'

r = session.get(url,headers=headers,allow_redirects=True) 

prods = r.html.xpath('//div[@data-component-type="s-search-result"]')

for p in prods:
    title= p.xpath('//div[@class="a-section a-spacing-none a-spacing-top-small"]/h2')[0].text
    price = p.xpath('//span[@class="a-price-whole"]')[0].text
    print(title)
    print(price)



# if title in splitted and attribute_p in title:
#     #if prod.text not in ['Carcasa', 'Funda', 'Protector', 'Soporte'] :
#     #if 'Carcasa' and 'Funda' and 'Protector' and 'Soporte' not in prod.text:
#     if 'carcasa' not in title and 'funda' not in title and 'protector' not in title and 'soporte' not in title:
#         print('match')
# else:
#     print('not found:')
#     print(r"\n")