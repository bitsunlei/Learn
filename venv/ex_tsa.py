# Time Series Analysis
# Reference: StatisticsMachineLearning Sec.9
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# A TS is said to be stationary if its statistics satisfy:
# Constant mean
# Constant variance
# An autocovariance that does not depend on time
# In contrast, there are 2 major reasons behind non-stationary TS:
# Trend- varying mean over time.
# Seasonality- variations at specific time-frames.

# A Series is equipped with additional functionality, methods, and
# operators compared with a list or an array.
# 1. index, 2, TS-values

x = pd.Series(np.arange(1,3),index=[x for x in 'ab'])
# print(x)

# import dataset
try:
    url = "https://raw.githubusercontent.com/datacamp/datacamp_facebook_live_ny_resolution/master/data/multiTimeline.csv"
    df = pd.read_csv(url,skiprows=2)
except:
    df = pd.read_csv("d:/python/data/multiTimeLine.csv",skiprows=2)
    print('Read CSV from downloaded file multiTimeLine.csv')

df.columns = ['Month', 'Diet', 'Gym', 'Finance']
print(df.head())

# plot figure using seaborn
import seaborn as sns

colors = sns.color_palette();
df.Month = pd.to_datetime(df.Month)
df.set_index('Month',inplace=True)

if False:
    # plt.figure('overview')
    df.plot(fontsize=16,figsize=(10,6),linewidth=5)
    plt.xlabel('Year',fontsize=20)
    plt.legend(loc='best')
    plt.show()

# df['Diet'].plot()
# for i in range(1,len(list(df.columns))):
#     plt.plot(df['Month'],df[df.columns[i]],color=colors[i],lw=2) #,label=df.columns[i])
# plt.legend('best')

diet = df['Diet']   # Series
diet_resamp_yr = diet.resample('A').mean()  # 'A': resample by year
diet_roll_yr = diet.rolling(12).mean()

if False:
    plt.figure(figsize=(9,6))
    ax0 = diet.plot(linewidth=3,alpha=0.3,style='-',label='Diet origin')
    diet_resamp_yr.plot(ax=ax0,style=':',lw=4,label='Diet resample by year')
    diet_roll_yr.plot(ax=ax0,style='-.',lw=4,label='Diet roll by year')
    plt.title('Diet',fontsize=16)
    plt.legend(loc='best',fontsize=16)
    plt.xlabel('Year',fontsize=16)
    plt.show()

# Rolling average with Numpy
x = np.asarray(df['Diet'])  # ndarray
win_size = 12
win_half = int(win_size/2)
# t= [((idx-win_half),(idx+win_half)) for idx in np.arange(win_half,len(x))]
diet_smooth= [x[(idx-win_half):(idx+win_half)].mean() for idx in np.arange(win_half,len(x))]
print(len(diet_smooth))
if False:
    plt.plot(diet_smooth)
    plt.show()

gym = df['Gym']
df_avg = pd.concat([diet.rolling(win_size).mean(),gym.rolling(win_size).mean()],axis=1)

# Detrending:
df_dtrend = df[df_avg.columns]-df_avg
if False:
    ax0 = df_avg.plot(label=df_avg.columns,fontsize=12,style=['-','-'],linewidth=3)
    df_dtrend.plot(ax=ax0,label=df_avg.columns,fontsize=12,style=[':',':'],linewidth=3)
    plt.xlabel('Year',fontsize=18)
    plt.show()

# Periodicity and Correlation
if False:
#    df.plot()
#    plt.xlabel('Year',fontsize=16)
    sns.heatmap(df.corr(),cmap='coolwarm')
    plt.show()

print(df.corr())
#             Diet       Gym   Finance
# Diet     1.000000 -0.100764 -0.034639
# Gym     -0.100764  1.000000 -0.284279
# Finance -0.034639 -0.284279  1.000000

# Trends and seasonal components decomposition
# Seasonal correlation is the correlation of the first-order difference
# of these time series
if False:
    # df.diff().plot(label=df_avg.columns,fontsize=12,linewidth=2)
    # plt.xlabel('Year',fontsize=16)
    sns.heatmap(df.diff().corr(),cmap='coolwarm')
    plt.title('Difference Correlation',fontsize=16)
    plt.show()
print(df.diff().corr())
#              Diet       Gym   Finance
# Diet     1.000000  0.758707  0.373828
# Gym      0.758707  1.000000  0.301111
# Finance  0.373828  0.301111  1.000000

# Decomposing time series in trend, seasonality and residuals
from statsmodels.tsa.seasonal import seasonal_decompose
x = df['Gym'].astype('float')
decomposition = seasonal_decompose(x)

trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

if False:
    plt.figure(figsize=(6,6))
    plt.subplot(411)
    plt.plot(x,label='Gym')
    plt.legend(loc='best')
    plt.subplot(412)
    plt.plot(trend,label='trend')
    plt.legend(loc='best')
    plt.subplot(413)
    plt.plot(seasonal,label='seasonal')
    plt.legend(loc='best')
    plt.subplot(414)
    plt.plot(residual,label='residual')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()

# Autocorrelation
# Autocorrelation function (ACF) is a measure of the correlation between the TS with a lagged
# version of itself. For instance at lag 5, ACF could compare series at time instant t1...t2
# with series at instant t1-5...t2-5
# Autocorrelation plot
from pandas.plotting    import autocorrelation_plot
x = df['Diet'].astype('float')
if False:
    autocorrelation_plot(x)
    plt.show()

# ACF calculation
from statsmodels.tsa.stattools import acf
x_diff  = x.diff().dropna()
lag_acf = acf(x_diff,nlags=36)
if False:
    plt.plot(lag_acf)
    plt.title('ACF',fontsize=16)
    plt.xlabel('ACF')
    plt.show()

# ARMA models
# In MA models, we assume that a variable is the sum of the mean of the time
# series and a linear combination of noise components.
# In general, an ARMA model with p autoregressive terms and q moving average terms
# as follows:
# x_t = \sum_i^p a_i x_{t-i} + \sum_j^q b_j eps_{t-j} + eps_t

# ARMA forecasting
# Plot the partial ACFs (PACFs) for an estimate of p, ACF functions for an estimate of q.
# PACF measures the correlation between the TS with a lagged version of itself but
# after eliminating the variations already explained by the intervening comparisons.
# Eg. at lag 5, it will check the correlation but remove the effects already explained
# by lags 1 to 4.
from statsmodels.tsa.stattools import acf,pacf
x = df['Gym'].astype('float')
x_diff = x.diff().dropna()

# acf and pacf
lag_acf = acf(x_diff,nlags=20)
lag_pacf = pacf(x_diff,nlags=20,method='ols')

if False:
    plt.subplot(121)
    plt.plot(lag_acf)
    plt.title('ACF (q=1)')

    plt.subplot(122)
    plt.plot(lag_pacf)
    plt.title('PACF (q=1)')
    plt.tight_layout()
    plt.show()

# Prediction with ARMA models
# 1. define the model by calling ARMA
# 2. The model is prepared on the training data by calling the fit() function
# 3. Predictions can be made by calling the predict() function and specifying
#    the index of the time or times to be predicted.
from statsmodels.tsa.arima_model import ARMA
x = df['Gym'].astype('float')
model = ARMA(x,order=(1,1)).fit()
print(model.summary())
if True:
    plt.plot(x,label = 'Gym original')
    plt.plot(model.predict(),color='red',label = 'predicted')
    plt.title('RSS: %.4f'%sum((model.fittedvalues-x)**2))
    plt.legend(loc='best')
    plt.show()

print('The End.')
