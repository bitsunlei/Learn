# Load stock real-time data
# 1大单压盘，2大单消亡，3股价向上 Deng 2018/08/08

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tushare as ts
import datetime as dt
import pathlib as pth
import time
from matplotlib.font_manager import FontProperties

print('Tushare Version '+ts.__version__)
if True:
    code_df   = pd.read_csv('d:/Python/data/stock_basics.csv',usecols=['code'],converters={'code':str})
    code_list = list(code_df['code']) #['%06d'%code_df[i] for i in range(0,len(code_df))]
else:
    code_start=   2000; code_range = 800
    code_list = ['%06d'%i for i in range(code_start,code_start+code_range)]

for ti in range(90):
    # break total codes into chunks for smooth downloading
    if True:
        if len(code_list)<500:
            rdf0 = ts.get_realtime_quotes(code_list[:500])  # Realtime DF
        else:
            chk_list = np.linspace(0,len(code_list),10).astype('int')  # break into chunks
            rdf0 = pd.DataFrame([])
        for i in range(0,len(chk_list)-1):
            print('%d'%chk_list[i]+' %d'%chk_list[i+1]+'downloading...')
            try:
                rdft = ts.get_realtime_quotes(code_list[chk_list[i]:chk_list[i+1]])  # get a chunk of data
                rdf0 = pd.concat([rdf0,rdft])
            except:
                print('Download exception and read data from saved file')
                rdf0 = pd.read_csv('d:/Python/data/realtime_quotes.csv')
                break
        print('%d'%len(code_list)+' codes downloaded')
        rdf0.to_csv('d:/Python/data/realtime_quotes.csv')
    else:
        rdf0 = pd.read_csv('d:/Python/data/realtime_quotes.csv',converters={'code':str})

    # remove non-used data
    rdf1 = rdf0.replace(to_replace='',value='0').copy()
    rdf  = rdf1[rdf1.open.astype('float')!=0.0].copy();    # remove unused stock codes
    rdf.set_index('code',inplace=True)

    # price rising compared by current prices with close prices on last day
    ris_val = (rdf.price.astype('float')-rdf.pre_close.astype('float'))*100/(rdf.pre_close.astype('float')+1e-6)

    # Define Dadan
    # 委卖单
    rising_th= 1.0    # define a threshold for selecting codes with price arising
    sell_list= ['a1_v','a2_v','a3_v','a4_v','a5_v']
    buy_list = ['b1_v','b2_v','b3_v','b4_v','b5_v']
    sell_vol = rdf.loc[ris_val>rising_th,sell_list].astype(float).copy()
    buy_vol  = rdf.loc[ris_val>rising_th,buy_list].astype(float).copy()

    # Calculate the deviation
    slct_max = sell_vol.max(axis=1)
    slct_mean= sell_vol.mean(axis=1)
    buy_mean= buy_vol.mean(axis=1)
    slct_idx = slct_max/(slct_mean+buy_mean)

    # Print selected codes information
    slct_sort = slct_idx.sort_values(ascending=False) # sorting the codes
    slct_codes= list(slct_sort.index)                 # extract the code index
    slct_lmt  = round(len(code_list)*0.005)           # extract a small part of the total codes
    slct_tdf = pd.DataFrame(data=slct_sort[:slct_lmt],columns=['PI'])
    slct_df  = pd.merge(rdf[['name','pre_close','price']],slct_tdf,how='inner',right_index=True,left_index=True)
    slct_df['change'] = (slct_df['price'].astype(float)/(slct_df['pre_close'].astype(float)+1e-6)-1)*100
    slct_df['change'] = slct_df['change'].apply(lambda x: '%.2f'%x)
    slct_df['time'] = dt.datetime.now().strftime('%H:%M')

    # save data to file
    slct_file   = pth.Path('d:/python/data/'+dt.datetime.now().strftime('%Y%m%d_pi.csv'))
    if slct_file.exists():
        with open(slct_file,'a',encoding='utf_8_sig') as f:
            slct_df.to_csv(f,header=False,encoding='utf_8_sig')
        print('selected codes appended to file')
        print(slct_df)
    else:
        slct_df.to_csv(slct_file,encoding='utf_8_sig')  #converters={'code':str})
        print('File created')

    print(ti,'th/60 processing ended, sleeping 60 seconds')
    time.sleep(60)    # sleep one minute

print('The End')
