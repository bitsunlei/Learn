
# Load stock real-time data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import tushare as ts
import datetime as dt

print('Tushare Version '+ts.__version__)
code_num = '000636'
try:
    rdf = ts.get_realtime_quotes(code_num)  # Realtime DF
    print(rdf)
    tdf = ts.get_today_ticks(code_num)      # Tick DF
    print(tdf)
except:
    print('Download exception')

# rdf.index = pd.to_datetime(rdf.date,format="%Y-%m-%d %H:%M")
# stk_today = rdf[rdf.index.date==dt.datetime(2018,8,7).date()].copy()

# tdf.index = pd.to_datetime(tdf.time,format="%H:%M:%S")
tdf = tdf[tdf['time']>'09:26:00']
tdf.index = pd.to_timedelta(tdf['time'])
mdf = tdf.resample('1Min',closed='left').mean().dropna()
if True:
    font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=16)
    fig,ax = plt.subplots(figsize=(20,16))
    plt.subplot(211)
    mdf['price'].plot(use_index=True, style='r-',linewidth=4,label='price',fontsize=16)
    plt.title(code_num+' '+rdf['name'].iloc[0],fontsize=20,fontproperties=font_set)
    plt.legend(loc='best')
    ax1 = plt.subplot(212)
    mdf['amount'].plot.bar(ax=ax1,style='b',linewidth=1,label='amount',fontsize=6)
    tk_gap = range(0,len(mdf),round(len(mdf)/8))
    ax1.set_xticks(ticks=tk_gap)
    ax1.set_xticklabels(labels=mdf.index[tk_gap],fontsize=12,rotation='vertical')
    plt.show()

if True:
    plt.figure(figsize=(8,8))
    mdf.plot.hexbin(x='price',y='amount',gridsize=20)
    plt.title(code_num+' '+rdf['name'].iloc[0],fontsize=20,fontproperties=font_set)
    plt.show()


print('The End')
