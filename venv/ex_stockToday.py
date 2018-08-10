# Stock Basics
# Load stock Today data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tushare as ts
import datetime as dt

print('Tushare Version '+ts.__version__)

if False:
    try:
        df=ts.get_stock_basics()
        df.to_csv('d:/Python/data/stock_basics.csv',encoding="utf_8_sig")
        df.to_excel('d:/Python/data/stock_basics.xls')
        print('Stock basics loaded and saved to a file')
    except:
        print('Stock basics loading failed')

rd=pd.read_csv('d:/Python/data/stock_basics.csv',usecols=['code'],converters={'code':str})
print(rd)



if False:
    code_num = '600519'
    try:
        stk_df = ts.get_k_data(code=code_num,start='2018-08-06',end='2018-08-07',ktype='5',autype='qfq')
    except:
        print('Download exception')

    stk_df.index = pd.to_datetime(stk_df.date,format="%Y-%m-%d %H:%M")
    stk_today = stk_df[stk_df.index.date==dt.datetime(2018,8,7).date()].copy()

# print(stk_df)

if False:
    plt.figure('Data')
    ax0=stk_today['volume'].plot(fontsize=16,style='-.',linewidth=4,logy=True)
    plt.title(code_num,fontsize=20)
    plt.xlabel('Today',fontsize=16)
    plt.show()

print('The End')
