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
    try:
        words = item.split(' ')
        new_words = []
        for word in words:
            word = word.capitalize() 
            new_words.append(word)
        item_p = ' '.join(new_words)

    except Exception as e:
        print(e)
        pass

    try:
        item_p = item.capitalize()
    except:
        pass

    if 'Iphone' or 'iphone' in item:
        item_p = item.replace('Iphone','iPhone').replace('iphone','iPhone')

    attribute_p = attribute.capitalize()

    print('maked data to match:',item_p,attribute_p)
    return item_p, attribute_p
    


def make_request(url):
    headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
    session = HTMLSession()
    r = session.get(url,headers=headers,allow_redirects=True)
    print('request made')
    return r


def get_matched_links(response,item_p,attribute_p,query):
    products_title = response.html.xpath('//div[@class="a-section a-spacing-none"]/div[@class="a-section a-spacing-none a-spacing-top-small"]/h2')
    #s = tag[0].text
    links = []
    for prod in products_title:
        #print(prod.text)
        if item_p in prod.text and attribute_p in prod.text:
            #if prod.text not in ['Carcasa', 'Funda', 'Protector', 'Soporte'] :
            #if 'Carcasa' and 'Funda' and 'Protector' and 'Soporte' not in prod.text:
            if 'Carcasa' not in prod.text and 'Funda' not in prod.text and 'Protector' not in prod.text and 'Soporte' not in prod.text:
                link = prod.absolute_links
                link = str(link)
                link = link.replace('{','').replace('}','')
                link = link.replace("'",'')
                #print({'query':query,'link':link})
                #entry = {'query':query,'link':link,'prod_title':prod.text}
                entry = (query,prod.text,' ',link)
                print(entry)
                links.append(entry)
        else:
            write_no_results(query)
    
    return links

def write_excel(links):
    wb = load_workbook(filename = 'matches.xlsx')
    ws = wb.active

    for entry in links:
        ws.append(entry)
        # #print(query,link,prod_title)
    separator = ('################################################','################################################','################################################','################################################')
    ws.append(separator)

    wb.save('matches.xlsx')


def write_no_results(query):
        
    wb = load_workbook(filename = 'no_results.xlsx')
    ws = wb.active
    entry = (query,'something_here')
    ws.append(entry)
    wb.save('no_results.xlsx')

item_attribute_list = []
def get_item_attribute():
    wb = load_workbook(filename = 'phones_color_variations.xlsx')
    ws = wb.active
 
    for row in ws.iter_rows(values_only=True):
        item = row[0]
        attribute = row[1]
        item_attribute_list.append({'item':item,'attribute':attribute})


get_item_attribute()
for element in item_attribute_list:

    item = element.get('item')
    attribute = element.get('attribute')

    print(item,attribute)

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
    links = get_matched_links(response, item_p,attribute_p,query)

    # write excel with query , prod_title , selection, link
    #selection is if the human validate that url has the needed pictures
    write_excel(links)
