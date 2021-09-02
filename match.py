from bs4 import BeautifulSoup as bs4
from requests_html import HTMLSession
import re

import xlsxwriter
from openpyxl.workbook.workbook import Workbook
from openpyxl import load_workbook


def make_query_url(item,attribute):
    query = item + ' ' + attribute
    #this is used for human reference in the file
    query_t = item + ' ' + attribute 
    query = query.replace(' ','+')

    #all deptartaments URL
    #url = 'https://www.amazon.es/s?k='+ query +'&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss'
    #Electronics URL
    url = 'https://www.amazon.es/s?k=' + query + '&i=electronics&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2'
    return url, query_t


def make_match_data(item,attribute):
    words = item.split(' ')
    new_words = []
    for word in words:
        word = word.capitalize() 
        new_words.append(word)
    item = ' '.join(new_words)

    if 'Iphone' in item:
        item = item.replace('Iphone','iPhone')

    attribute = attribute.capitalize()
    return item, attribute


def make_request(url):
    headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
    session = HTMLSession()
    r = session.get(url,headers=headers,allow_redirects=True)
    return r


def get_matched_links(response):
    products_title = response.html.xpath('//div[@class="a-section a-spacing-none"]/div[@class="a-section a-spacing-none a-spacing-top-small"]/h2')
    #s = tag[0].text
    links = []
    for prod in products_title:
        #print(prod.text)
        if item_p and attribute_p in prod.text:
            link = prod.absolute_links
            #print({'query':query,'link':link})
            #entry = {'query':query,'link':link,'prod_title':prod.text}
            entry = (query,link,prod.text)
            links.append(entry)
    
    return links

row_n = 1
col_n = 1
def write_excel(links):
    global row_n
    global col_n

    wb = load_workbook(filename = 'matches.xlsx')
    ws = wb.active

    for entry in links:
        #query = entry.get('query')
        #prod_title = entry.get('prod_title')
        #link = str(entry.get('link')).replace('{','').replace('}','')
        
        ws.append(entry)
        # #print(query,link,prod_title)
    
        # ws.cell(row=row_n,column=col_n,value = query)
        # ws.cell(row=row_n,column=col_n + 1 ,value = prod_title)
        # ws.cell(row=row_n,column=col_n + 3 ,value = link.strip("'"))

        # row_n += 1
    
    wb.save('matches.xlsx')
    # for row in ws.iter_rows(values_only=True):
    #     if row[0] != None:
    #         pass


#take the item and its attribut from target_prods
item = 'iPhone 12 pro' #Pro
attribute = 'grafito'



#process the item and the attribute to match Amazon's standart (Capitalization, iPhone,etc...)
#This is used later to identify matches within the titles of the prods.
# _p means processed: from 'iphone pro' to 'iPhone Pro'
item_p,attribute_p = make_match_data(item,attribute)

#with the above data make the url and the query (used later in the excel)
url, query = make_query_url(item_p,attribute_p)

#make the request with the query
response = make_request(url)

#extract the links of the products which titles matches the query
#list of dicts with link , query, prod_title
links = get_matched_links(response)

# write excel with query , prod_title , selection, link
#selection is if the human validate that url has the needed pictures
write_excel(links)

# r = make_request(url)
# status = r.status_code
# #To visualize response in the browser
# #save_html_response(r)
# if status == 200:
#     links = get_links(r)
# else:
#     print("Response status:{} for the query {} and url: {}".format(status,query,url))
    
#links = [{'lins1':'at1'},{'lins2':'at2'},{'lins3':'at3'}]
