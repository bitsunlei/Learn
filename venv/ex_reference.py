花了半天时间在 MINDGO 量化交易平台的研究环境中绘制了 K 线图，并进行了分析，有兴趣的可以到 MINDGO 量化交易平台上学习画 K 线图，并分析，如有疑难，加入 MINDGO 量化交流群：217901996. 对学 Python 绘图包有兴趣的可以加一波
K 线图源代码：
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick2_ohlc
import datetime
data=get_price(['000300.SH'], None, '20171110', '1d', ['open','high','low','close'], True, None, 200, is_panel=0)
data=data['000300.SH']
#时间转化格式
time=data.index
t=[]
for x in time:
x=str(x).split()[0]
x=x.split('-')
x=x[0]+x[1]+x[2]
x=int(x)
t.append(x)
#画图数据
time=t
open1=list(data['open'])
high1=list(data['high'])
low1=list(data['low'])
close1=list(data['close'])
#画图
fig,ax = plt.subplots(figsize = (32,8),facecolor='pink')
fig.subplots_adjust()
plt.xticks()
plt.yticks()
plt.title("沪深 300K 线走势图")
plt.ylabel("股指")
ticks = ax.set_xticks(range(1,200,40))
labels = ax.set_xticklabels([time[0],time[40],time[80],time[120],time[160]])
candlestick2_ohlc(ax,open1,high1,low1,close1,width=0.6,colorup='red',colordown='green')
#支撑线
plt.plot([75,200],[3316,3954],'g',linewidth=10)
# 红星：回踩 1
plt.plot(75, 3316, 'r*', markersize = 40.0,label='趋势线')
plt.annotate(r'二次低位', xy=(75, 3316),
xycoords='data', xytext=(-90, -50),
textcoords='offset points', fontsize=26,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
# 红星：回踩 2
plt.plot(140, 3650, 'r*', markersize = 40.0)
plt.annotate(r'止跌，形成趋势线', xy=(140, 3650),
xycoords='data', xytext=(-90, -50),
textcoords='offset points', fontsize=26,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
# 红星：回踩 3
plt.plot(172, 3800, 'r*', markersize = 40.0)
plt.annotate(r'回踩趋势线', xy=(172, 3800),
xycoords='data', xytext=(-90, -50),
textcoords='offset points', fontsize=26,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
#MA5
data['ma5']=pd.rolling_mean(data['close'],5)
plt.plot(list(data['ma5']),label='五日均线')
#MA10
data['ma10']=pd.rolling_mean(data['close'],10)
plt.plot(list(data['ma10']),label='十日均线')
#MA20
data['ma20']=pd.rolling_mean(data['close'],20)
plt.plot(list(data['ma20']),label='二十日均线')
#MA30
data['ma30']=pd.rolling_mean(data['close'],30)
plt.plot(list(data['ma30']),label='三十日均线')
#MA60
data['ma60']=pd.rolling_mean(data['close'],60)
plt.plot(list(data['ma60']),label='六十日均线')
plt.legend()
print('沪深 300 走势图分析')

成交量源代码：
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams
data=get_price(['000300.SH'], None, '20171110', '1d', ['volume'], True, None,200, is_panel=0)['000300.SH']
data['volma5']=pd.rolling_mean(data['volume'],5)
data['volma10']=pd.rolling_mean(data['volume'],10)
volma5=list(data['volma5'])
volma10=list(data['volma10'])
data['goldordie']=(data['volma5']-data['volma10'])
time=data.index
t=[]
for x in time:
x=str(x).split()
x=x[0]
t.append(x)
#画图数据
time=t
x=list(data['volume'])
y=len(x)
z=range(0,y,1)
fig,ax = plt.subplots(figsize = (48,8),facecolor='pink')
ticks = ax.set_xticks(range(1,200,40))
rects =plt.bar(left = z,height = x,width = 0.4,color=('r','g'),align="center",yerr=0.1)
plt.title('VOL')
# plt.xticks(z,t)
# 蓝线：五日量能
plt.plot(volma5,'b',label="五日量能")
# 蓝线：十日量能
plt.plot(volma10,'y',label="十日量能")
plt.title("沪深 300 成交量")
print("沪深 300 成交量")
jc=[]
sc=[]
for x in range(0,200,1):
z=x-1
y2=data['goldordie'].iloc[x]
y1=data['goldordie'].iloc[z]
if y1<0 and y2>0:
jc.append(x)
elif y1>0 and y2<0:
sc.append(x)
for x in jc:
if x== jc[-1]:
vol=data['volma5'].iloc[x]
plt.plot(x, vol, 'r*', markersize = 40.0,label='金叉')
else:
vol=data['volma5'].iloc[x]
plt.plot(x, vol, 'r*', markersize = 40.0)
for x in sc:
if x==sc[-1]:
vol=data['volma5'].iloc[x]
plt.plot(x, vol, 'g*', markersize = 40.0,label='死叉')
else:
vol=data['volma5'].iloc[x]
plt.plot(x, vol, 'g*', markersize = 40.0)
plt.legend()
plt.show()
MACD 指标源代码：
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams
data=get_price(['000300.SH'], None, '20171110', '1d', ['close'], True, None,233, is_panel=0)['000300.SH']
data['ma12']=pd.ewma(data['close'],12)
data['ma26']=pd.ewma(data['close'],26)
data['diff']=data['ma12']-data['ma26']
data['dea']=pd.ewma(data['diff'],9)
data['macd']=data['diff']-data['dea']
data=data[33:]
diff=list(data['diff'])
dea=list(data['dea'])
fig,ax=plt.subplots(figsize=(16,4),facecolor='pink')
plt.plot(diff,'b',label='diff')
plt.plot(dea,'y',label='dea')
macd=list(data['macd'])
x=len(list(data['macd']))
x=range(0,x,1)
rects =plt.bar(left = x,height = macd,width = 0.4,color=('g','r'),align="center",yerr=0.1)
plt.title('MACD 指标')
jc=[]
sc=[]
data['goldordie']=data['diff']-data['dea']
for x in range(0,200,1):
z=x-1
y2=data['goldordie'].iloc[x]
y1=data['goldordie'].iloc[z]
if y1<0 and y2>0:
jc.append(x)
elif y1>0 and y2<0:
sc.append(x)
for x in jc:
if x==jc[-1]:
diff=data['diff'].iloc[x]
if diff>0:
plt.plot(x, diff, 'r*', markersize = 20.0,label='金叉')
plt.annotate(r'多方金叉顺势买入', xy=(x, diff),
xycoords='data', xytext=(-20, -20),
textcoords='offset points', fontsize=12,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
else:
plt.plot(x, diff, 'r*', markersize = 20.0,label='金叉')
plt.annotate(r'空方金叉猥琐买入', xy=(x, diff),
xycoords='data', xytext=(-20, -20),
textcoords='offset points', fontsize=12,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
else:
diff=data['diff'].iloc[x]
if diff>0:
plt.plot(x, diff, 'r*', markersize = 20.0)
plt.annotate(r'多方金叉顺势买入', xy=(x, diff),
xycoords='data', xytext=(-20, -20),
textcoords='offset points', fontsize=12,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
else:
plt.plot(x, diff, 'r*', markersize = 20.0)
plt.annotate(r'空方金叉猥琐买入', xy=(x, diff),
xycoords='data', xytext=(-20, -20),
textcoords='offset points', fontsize=12,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
for x in sc:
if x==sc[-1]:
diff=data['diff'].iloc[x]
if diff >0:
plt.plot(x, diff, 'g*', markersize = 20.0,label='死叉')
plt.annotate(r'多方死叉猥琐卖出', xy=(x, diff),
xycoords='data', xytext=(20, 20),
textcoords='offset points', fontsize=12,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
if diff <0:
plt.plot(x, diff, 'g*', markersize = 20.0,label='死叉')
plt.annotate(r'空方死叉顺势卖出', xy=(x, diff),
xycoords='data', xytext=(20, 20),
textcoords='offset points', fontsize=12,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
else:
diff=data['diff'].iloc[x]
if diff>0:
plt.plot(x, diff, 'g*', markersize = 20.0)
plt.annotate(r'多方死叉猥琐卖出', xy=(x, diff),
xycoords='data', xytext=(10, 20),
textcoords='offset points', fontsize=12,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
else:
plt.plot(x, diff, 'g*', markersize = 20.0)
plt.annotate(r'空方死叉顺势卖出', xy=(x, diff),
xycoords='data', xytext=(10, 20),
textcoords='offset points', fontsize=12,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.legend()