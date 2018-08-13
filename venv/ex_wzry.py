# Load and analyze WZRY Game Data.
# Sun Lei. 2018-08-12

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tushare as ts
import datetime as dt
import pathlib as pth
import time
from matplotlib.font_manager import FontProperties

# load data for analysis
rd_file = pth.Path('D:/BaiduNetdiskDownload/data/wangzhe/wzry_1000items.data')
if rd_file.exists()==False:
    print('Data file does not exist')
rdf   = pd.read_csv(rd_file,sep='#',header=None,nrows=10,
                    names=['SubaoIP','UserIP','GameIP','time','before','after'])
rdf['time']=pd.to_datetime(rdf['time'],format= '%Y-%m-%dT%H:%M:%SZ')

# check the time delay values
idx  = 0
for idx in range(len(rdf)):
    bf_list = rdf.loc[idx,'before']
    af_list = rdf.loc[idx,'after']
    bf_ary = np.fromstring(bf_list[1:-1],dtype=int,sep=',')
    af_ary = np.fromstring(af_list[1:-1],dtype=int,sep=',')
    data   = [bf_ary,af_ary]
    labels = ['Before','After']
    colors =['pink','lightgreen']

    fig,ax = plt.subplots(figsize=(3,5))
    bplot1 = plt.boxplot(data, notch=False, vert=True, patch_artist=True, labels=labels,
                sym='b+',widths=0.2, meanline=True,showmeans=True)
    plt.title(str(rdf.loc[idx,'time'])+'\n ('+rdf.loc[idx,'SubaoIP']+'--'+rdf.loc[idx,'GameIP']+')')
    #plt.legend(loc='best')
    plt.gca().set_xticklabels(['before','after'],rotation='horizontal',fontsize=16)
    for patch,color in zip(bplot1['boxes'],colors):
        patch.set_facecolor(color)
    #plt.show()
    fig.savefig('D:/BaiduNetdiskDownload/data/wangzhe/jpeg/'+'%04d_'%idx+'box.jpg')
    print(idx,'th figure saved')
    plt.close(fig)

print('The End')
