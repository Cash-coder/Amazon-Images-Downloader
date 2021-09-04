from openpyxl import load_workbook
from openpyxl.workbook.workbook import Workbook

item_attribute_list = []
wb = load_workbook(filename = 'tablets.xlsx')
ws = wb.active

n = 1
for row in ws.iter_rows(values_only=True):
    item = row[0]
    if item != None:
        item = item.replace('(','').replace(')','') #ipad pro (2021)
        try:
            if 'GB' in item:
                chain = item.split(' ')
                chain.pop()
                chain.pop()
                item = " ".join(chain)
                #chain = chain.remove(chain[-1])
                #chain = chain.remove(chain[-2])

                print(item)
                #myList.remove(myList[len(myList)-1])
            else:
                print(item)
            
            # print('going to print')
            wb = load_workbook(filename='p_tablets.xlsx')
            ws = wb.active
            ws.cell(row=n,column=1,value=item)
            wb.save('p_tablets.xlsx')
            n += 1
            # print('printed')

        except Exception as e:
            print(e)
            continue
