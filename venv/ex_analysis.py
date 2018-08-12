# Load and analyze the stored stock data. Dependency: ex_scanner.py
# 1大单压盘，2大单消亡，3股价向上 Deng 2018/08/08

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tushare as ts
import datetime as dt
import pathlib as pth
import time
from matplotlib.font_manager import FontProperties

# load data for analysis
rd_file = pth.Path('d:/python/data/'+dt.datetime.now().strftime('%Y%m%d_test.csv'))
if rd_file.exists()==False:
    rd_file = pth.Path('d:/python/data/20180810_test.csv')
rd_df   = pd.read_csv(rd_file,converters={'code':str})
rd_df['code'] = rd_df['code'].apply(lambda x: '%06d'%(int(x)))  # formatting the code column

def grpdata_process(gp,rd_df):
    gp_sort = gp.size().sort_values(ascending=False)
    idxs_lim = 20           # set the limit for selecting a part of all
    gp_idxs = gp_sort[:idxs_lim]
    gp_mdf = pd.DataFrame(data=None,index=gp_idxs.index,columns=['name','count','PI','change'])
    for i in range(len(gp_idxs)):
        gpi_m = gp.get_group(gp_idxs.index[i]).mean()
        gp_mdf.loc[gp_idxs.index[i],'name']  = rd_df[rd_df.code == gp_mdf.index[i]]['name'].iloc[0]
        gp_mdf.loc[gp_idxs.index[i],'count'] = gp_idxs[i]
        gp_mdf.loc[gp_idxs.index[i],'PI']    = '%.2f'%gpi_m['PI']
        gp_mdf.loc[gp_idxs.index[i],'change']= '%.2f'%gpi_m['change']
    return gp_mdf

# group the data by 'code' with its appearance counts
gp      = rd_df[['code','PI','time','change']].groupby('code')
gp_mdf  = grpdata_process(gp,rd_df)
gp_mdf.to_csv(str(rd_file).replace('test','ana'),encoding='utf_8_sig')

# check the history data of these code
code_check = gp_mdf.index[4]
cd_df = ts.get_k_data(code_check,start='2018-07-30',end='2018-08-10')
title = cd_df['code'].iloc[0] # +cd_df.loc[0,'name']
cd_df.set_index('date',inplace=True)
cd_df.drop(['volume','code'],axis=1,inplace=True)

# plt.figure()
fig,ax=plt.subplots(figsize=(9,4))
cd_df.plot.area(ax=ax,stacked=False)
plt.gca().set_ylim(cd_df.min().min(),cd_df.max().max())
plt.gca().set_xticks(list(range(len(cd_df))))
plt.gca().set_xticklabels(cd_df.index,rotation='vertical')
plt.gca().set_title(title)
plt.show()
fig.savefig('d:/python/data/jpeg/'+title+'_10days.jpg')



if False:
    fig,ax=plt.subplots(figsize=(10,8))
    for i in range(15,len(gp_slct)):
        gp_df = gp.get_group(gp_slct.index[i])
        gp_df.set_index('time', inplace=True)
        #plt_gp= gp_df.rename(columns={'PI':gp_df.code[0]})
        plt.plot(gp_df.index,gp_df.PI,'o',label=gp_df.code[0])
        #plt_gp.plot(ax=ax)

    plt.legend(loc='best')
    plt.show()

print('The End')
