#https://pypi.org/project/mega.py/
from mega import Mega
import login_file # .py file with MEGA user and password
from requests_html import HTMLSession
import requests
import re
from time import sleep
from openpyxl import load_workbook
from openpyxl.workbook.workbook import Workbook
import os

#init mega
email = login_file.email
password = login_file.passw

print(email, password)

input_file  = 'phones_set.xlsx'
output_file = 'processed_items.xlsx'
errors_file = 'errors.xlsx'

#local windows
pics_folder =  r'C:/Users/HP EliteBook/OneDrive/A_Miscalaneus/Escritorio/Code/git_folder/images_downloader/down_send/pics_folder/'
#server
#pics_folder = '/home/nonroot/pics/s_pics/down_send/pics_folder/'

#returns a list of dicts with {item , url}
def extract():
    wb = load_workbook(filename = input_file)
    ws = wb.active
    target_list = []
    #item_attribute_list = []
    for row in ws.iter_rows(values_only=True):
        item = row[0]
        url = row[1]

        entry = {'item':item, 'url':url}
        target_list.append(entry)
        # if 'GB' in item:
        #     chain = item.split(' ')
        #     item_p = chain.remove(chain[-1])
        #     item_p = chain.remove(chain[-2])
        #     print(item_p)
        #     #myList.remove(myList[len(myList)-1])
    return target_list

# def make_query(item):
#     query = item.replace(' ', '+')
#     return query

n_errors = 1
def write_bad_result(url,item='no item appended'):
    global n_errors

    wb = load_workbook(filename = errors_file)
    ws = wb.active

    ws.cell(row=n_errors,column=1,value=item)
    ws.cell(row=n_errors,column=2,value=url)

    n_errors += 1



def download_picture(url, item, n): # Download To local machine
    ''' download from url, name file with item + n'''
    global pics_folder
    try:
        pic = requests.get(url)

        if pic.status_code == 200:
            file_name = item + ' ' + str(n) +'.jpg'
            file_name = file_name.replace(' ','_')
    
            try:
                
                complete_path = pics_folder + file_name
                
                with open(complete_path, 'wb') as f:
                    f.write(pic.content)
                    print('downloaded this pic: ',file_name)
            except Exception as e:
                print(e)
                print('failed to save this pic',item, url)
                write_bad_result(item,url)
        else:
            write_bad_result(item,url)
            
    except Exception as e:
        print(e)
        write_bad_result(item,url)
        save_html_response(pic,item)


        
def save_html_response(r,item):
    item = item.replace(' ', '_')
    with open(item + 'response.html','w',encoding='utf-8') as f:
        f.write(r.text)


def get_pictures_urls(url):
    ''' returns a list with image URL's picks the url from Amazon or Backmarket'''
    url_list = []

    headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
    session = HTMLSession()
    r = session.get(url,headers=headers,allow_redirects=True)
    
    status = r.status_code
    if status != 200:
        print('status code error, status: ',status)
        write_bad_result(url=url)
        return
    
    # Backmarket image links picker
    if 'backmarket' in url:
        tags = r.html.xpath('//div[@data-test="thumb-carousel"]/@style')
        n = 0
        for url in tags:
            url = url.replace('background-image:url(','').replace(');','').replace("'","")
            print(' This url has been findend and appended to list',url) 
            url_list.append(url)

    # Amazon image links picker
    elif 'amazon' in url:
        tag = r.html.find('script', containing='P.when(\'A\').register("ImageBlockATF", function(A){')
        s = tag[0].text
        # hiRes == High Resolution 
        # main  ==  ?
        # large ==  ?
        matches = re.findall(r'hiRes(.*?).jpg', s)
        for match in matches:
            if match == None :
                print('----- founded NONE match in this tag', s)
                print('-------------------------- tag ends here -------------------')
                continue
            
            if '{' in match:
                url = match.replace('":{"','') + '.jpg'
            else:
                url = match.replace('":"','') + '.jpg'

            url_list.append(url)  
            print(' This url has been findend and appended to list',url) 
    
    return url_list

def raw_request(url):
    ''' unused, testing new get_pictures_urls() to delete this old func'''
    headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
    session = HTMLSession()

    r = session.get(url,headers=headers,allow_redirects=True)
    status = r.status_code
    #To visualize response in the browser
    #save_html_response(r)
    if status == 200:
        tag = r.html.find('script', containing='P.when(\'A\').register("ImageBlockATF", function(A){')
        s = tag[0].text
    else:
        print("Response status:{} for the url: {}".format(status,url))

    return s

n_write = 1
def write_file(url_list,item):
    '''write when action performed without errors'''
    global n_write

    wb = load_workbook(filename=output_file)
    ws = wb.active

    for url in url_list:#ws.iter_rows(values_only=True):
        ws.cell(row=n_write, column=1, value=item)
        ws.cell(row=n_write, column=2, value=url)
        n_write += 1
        wb.save(output_file)
    # with open('URLs.csv','w') as f:
        # fieldnames = ['Title','URL']
        # writer = csv.DictWriter(f,fieldnames=fieldnames)
        # writer.writeheader()
        
        # n = 0 #used to identify the picture 
        # for item_url in url_list:
            # title = 'query_test' + str(n)
            # n +=1
            # writer.writerow({'Title':title,'URL':item_url})

def send_mega():
    ''' send all files from pics_folder to mega'''
    #crete a list with all the file paths
    file_list = []
    for root, dirs, files in os.walk(pics_folder):
        for file in files:
            file_path = root + file 
            file_list.append(file_path)

    mega = Mega()
    m = mega.login(email, password)
    folder = m.find('IMAGES')
    #upload files
    for file in file_list:
        m.upload(file, folder[0])
        print('uploaded to mega this file: ', file)

def delete():
    '''deletes all the files in pics_folder, to declutter it'''
    filelist = [ f for f in os.listdir(pics_folder)]#if f.endswith(".bak") ]
    for f in filelist:
        os.remove(os.path.join(pics_folder, f))

def run():
    targets_list = extract() #get items and url's from excel file

    for e in targets_list:

        item = e.get('item')
        url = e.get('url')

        #query = make_query(item)
        #raw_data = raw_request(url)

        url_list = get_pictures_urls(url)
        #for url in url_list:
            #download_picture(url)
        #write_file(url_list,item)  
        n_name = 0 # used to name the downloads, iphone_verde_1, verde_2....
        for pic in url_list:
            if pic == None :
                print('in run loop, founded None url')
                continue

            download_picture(pic, item,n_name) #item used to set the name
            n_name += 1
            sleep(3)
        
        send_mega()

        delete()



if __name__ == "__main__":
    run()
