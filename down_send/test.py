l= [200,200,503,503,200,123]
retries = 0
n = 0
while retries < 6:
    
    status = l[n]
    n += 1
    if status == 503:
        print('status code 503, going to retry')
        retries += 1
        
    elif status != 200:
        #print('status code error, status: ',status)
        #write_bad_result(url, item)
        
        #return 'request error'
        print('not 200')
    elif status == 200: 
        print('good')