import requests
from io import StringIO
import pandas as pd
import numpy as np
import time
import xlwt

datestr='20180326'

r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')
df = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '}) 
for i in r.text.split('\n') 
if len(i.split('",')) == 17 and i[0] != '='])), header=0)

xls = xlwt.Workbook()  #建立Workbook
sheet=xls.add_sheet(datestr) #建立分頁

lr=df.shape[0]  
lc=df.shape[1]
row=0
column=0

while column<lc:
    sheet.write(0,column,df.columns[column])
    column+=1

while row < lr:
    column=0
    while column < lc:     
        sheet.write(row+1,column,df.iloc[row,column])
        column+=1
    row+=1

xls.save('TWStock_'+ datestr + '.xls') #儲存Workbook檔名為TWStock.xls

