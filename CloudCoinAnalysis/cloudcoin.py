#!/usr/bin/env python
# coding: utf-8

# # Analysis of Cryptocurrency Investments

#
# In this analysis report, I will perform exploratory data analysis and build machine learning models to predict market prices in future 30 days for the above 7 cryptocurrencies.

# [1. Prepare Data Set](#1)
#  - [Load Python Packages](#1-1)
#  - [Load and Prepare Data Set](#1-2)
#
# [2. Data Quality Assessment](#2)
#  - [Check Missing Values](#2-1)
#  - [Check Duplicated Values](#2-2)
#
# [3. Exploratory Data Analysis and Feature Engineering](#3)
#  - [1.Market Capitalization and Transaction Volume](#3-1)
#  - [2.Price Fluctuation of Cryptocurrencies](#3-2)
#  - [3.Moving Averages and Price Trend](#3-3)
#  - [4.Market Prices of Cryptocurrencies](#3-4)
#  - [5.Return Ratio](#3-5)
#  - [6.Candlestick Charts Using Plotly (BitCoin)](#3-6)
#
# [4. Building Models - Predicting Price for Cryptocurrencies](#4)
#  - [Prepare Data for Models](#4-1)
#  - [Applying Machine Learning Models](#4-2)
#  - [Prices Prediction](#4-3)
#
# [5. Conclusion - Investment Suggestion](#5)
#
# [6. Future Work](#6)
#
# [7. Reference](#7)
#

# ***

# ## 1. Prepare Data Set<a id="1"></a>

# ### Load Python Packages<a id="1-1"></a>

import numpy as np
import pandas as pd
import datetime as dt

import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

import matplotlib.pyplot as plt
import seaborn as sns; sns.set_style("whitegrid")
from plotly import tools
import plotly.offline as py
import plotly.io as io
#py.init_notebook_mode(connected=True)
import plotly.graph_objs as go

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor
from sklearn.linear_model import BayesianRidge, ElasticNetCV
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

import sys
dir=sys.argv[1];
datafile=sys.argv[2];

# ### Load and Prepare Data Set<a id="1-2"></a>

# load data set
data = pd.read_csv(datafile, parse_dates=['date'],index_col='date')

#
current_date = data.index[len(data)-1];
print("current date : " + str(current_date))
title_tstamp = ( " \n[ updated on " + str(current_date) + " ]");

# display appointment data set
data.head();

data = data[data.symbol.isin(['BTC','SNM', 'GNT', 'RLC'])]

# display total number of records for the 7 cryptocurrencies
data.name.value_counts()

# display data volumn and types
data.info()

# ## 2. Data Quality Assessment<a id="2"></a>

# ### Check Missing Values<a id="2-1"></a>

# check if data set contains missing values
print(data.isnull().sum())

# assert that there are no missing values
assert data.notnull().all().all()


# No missing value exist in this data set.

# ### Check Duplicated Values<a id="2-2"></a>

# check if data set contains duplicated records
print(data.duplicated().sum())

# There is no duplicated appointments record in this data set. The data is clean.

# ## 3. Exploratory Data Analysis and Feature Engineering<a id="3"></a>

# ### Market Capitalization and Transaction Volume<a id="3-1"></a>

# Check market capitalization and transaction volume for each cryptocurrency we choose.

# plot market capitalization

rlc = data[data['symbol']=='RLC']
gnt = data[data['symbol']=='GNT']
snm = data[data['symbol']=='SNM']

plt.figure(figsize=(15,8))
#(bitcoin['market']/1000000).plot(color='darkorange', label='Bitcoin')
(rlc['market']/1000000).plot(color='darkorange', label='iExec')
(gnt['market']/1000000).plot(color='grey', label='GOLEM')
(snm['market']/1000000).plot(color='blue', label='sonM')

plt.legend()
plt.xlabel('date')
plt.ylabel('Market cap in Million US Dollar')
plt.title('Cloud Computing Cryptocurrency Market Cap)' + title_tstamp)

plt.savefig(dir + "Cryptocurrency_Market_Cap")


## volume 2019

data_m = data['2019-01-01':'2019-04-15']
rlc = data_m[data_m['symbol']=='RLC']
gnt = data_m[data_m['symbol']=='GNT']
snm = data_m[data_m['symbol']=='SNM']

plt.figure(figsize=(15,8))

(rlc['market']/1000000).plot(color='darkorange', label='iExec')
(gnt['market']/1000000).plot(color='grey', label='GOLEM')
(snm['market']/1000000).plot(color='blue', label='sonM')
#plt.axvline(dt.datetime(2019, 12, 12),color='black')

plt.legend()
plt.xlabel('time')
plt.title('Cryptocurrency Transaction Volume (Million) in 2019' + title_tstamp)
#plt.show()
plt.savefig(dir + 'Cryptocurrency_Transaction_Volume_in_2019')


data = data['2019-01-01':]

# Check opening, closing, highest, and lowest price for each of the cryptocurrency.


data['oc_diff']=data['close']-data['open']
data.head()


# Difference between opening and closing price
data['oc_diff']=data['close']-data['open']
rlc = data[data['symbol']=='RLC']
gnt = data[data['symbol']=='GNT']
snm = data[data['symbol']=='SNM']

plt.figure(figsize=(15,8))
(rlc['oc_diff']).plot(color='darkorange', label='RLC')
(gnt['oc_diff']).plot(color='grey', label='GNT')
(snm['oc_diff']).plot(color='blue', label='SNM')
plt.text(20,0.05,'test',verticalalignment='bottom', horizontalalignment='center', fontsize=15)
plt.xlabel('time')
plt.ylabel('price in USD')
plt.title('Historical difference between daily opening price and daily closing price of the 3 cloud Cryptocurrencies since 2019' + title_tstamp)


plt.legend()
#plt.show()
plt.savefig(dir + 'Historical_difference_between_opening_price_and_closing_price_of_cloud_Crypto_since_2019')

# Average difference for each cryptocurrency
ave_diff={'rlc':[(rlc['oc_diff']).mean()],
          'gnt':[(gnt['oc_diff']).mean()],
          'snm':[(snm['oc_diff']).mean()]}
pd.DataFrame(ave_diff, index=['avg.diff'])

# To get a better understanding of difference between daily opening and closing price,
# we calculated the average difference as well as daily price spread for each cryptocurrency.

# Differences of daily highest price and lowest price
plt.figure(figsize=(15,8))

(rlc['spread']).plot(color='grey', label='RLC')
(gnt['spread']).plot(color='blue', label='GNT')
(snm['spread']).plot(color='green', label='SNM')

plt.xlabel('time')
plt.ylabel('price in USD')
plt.title('Historical daily price spread of cloud Crypto,\n indicator of value variation' + title_tstamp)
plt.legend()
#plt.show()
plt.savefig(dir + 'Historical_price_spread_of_cloud_Crypto')

# By plotting the spread (difference) between daily highest and lowest price, we found that:

# Average spread for each cryptocurrency
ave_spread={'rlc':[(rlc['spread']).mean()],
          'gnt':[(gnt['spread']).mean()],
          'snm':[(snm['spread']).mean()]}
pd.DataFrame(ave_spread, index=['avg.spread'])

# calculate 5-day moving averages
_rlc = rlc[['close']]
_rlc.columns = ['RLC']
rlc_ma=_rlc.rolling(window=5).mean()

_gnt = gnt[['close']]
_gnt.columns = ['GNT']
gnt_ma=_gnt.rolling(window=5).mean()

_snm = snm[['close']]
_snm.columns = ['SNM']
snm_ma=_snm.rolling(window=5).mean()

# create matrix of close price only for later use
close = pd.concat([_rlc,_gnt,_snm], axis=1)
close_ma = pd.concat([rlc_ma,gnt_ma,snm_ma], axis=1)
close_ma.tail()

# plot moving average for closing price for cryptocurrencies
close_ma.plot(figsize=(15,8))
plt.title('5-Day Moving Average on Daily Closing Price, fluctuation indicator' + title_tstamp)
plt.xlabel('time')
plt.ylabel('price in USD')

plt.savefig(dir + '5-Day_Moving_Average_on_Daily_Closing_Price')

# calculate daily average price
data['daily_avg'] = (data['open'] + data['high'] + data['low'] + data['close']) / 4
bitcoin = data[data['symbol']=='BTC']
rlc = data[data['symbol']=='RLC']
gnt = data[data['symbol']=='GNT']
snm = data[data['symbol']=='SNM']

plt.figure(figsize=(15,8))
#(bitcoin['daily_avg']).plot(color='brown', label='btc')
(rlc['daily_avg']).plot(color='grey', label='rlc')
(gnt['daily_avg']).plot(color='blue', label='gnt')
(snm['daily_avg']).plot(color='yellow', label='snm')

plt.xlabel('time')
plt.ylabel('price in USD')
plt.title('Historical daily average price of cloud Crypto,\n (open+high+low+close)/4' + title_tstamp)
plt.legend()
#plt.show()
plt.savefig(dir + 'Historical_daily_average_price_of_cloud_Crypto_since_2019')

# #### Plot individual daily open, high, low, close prices

plt.figure(figsize=(15, 12))
plt.subplot(4,1,1)
plt.plot(bitcoin[['open','high','low','close']])
plt.ylabel('price in USD')
plt.title('Historical daily average price of BitCoin since 2019'+ title_tstamp)
plt.legend(['open','high','low','close'])
plt.subplot(4,1,2)
plt.plot(rlc[['open','high','low','close']])
plt.ylabel('price in USD')
plt.title('Historical daily average price of RLC since 2019'+ title_tstamp)
plt.legend(['open','high','low','close'])

plt.subplot(4,1,3)
plt.plot(gnt[['open','high','low','close']])
plt.ylabel('price in USD')
plt.title('Historical daily average price of GNT since 2019'+ title_tstamp)
plt.legend(['open','high','low','close'])

plt.subplot(4,1,4)
plt.plot(snm[['open','high','low','close']])
plt.ylabel('price in USD')
plt.title('Historical daily average price of SNM since 2019'+ title_tstamp)
plt.legend(['open','high','low','close'])

#plt.show()
plt.savefig(dir + "Plot_individual_daily_open_high_low_close_prices")

# #### Check Pearson correlation coefficient to prove if BitCoin price influences price of other cryptocurrencies

plt.figure(figsize=(12,6))
sns.heatmap(close.corr(),vmin=0, vmax=1, cmap='coolwarm', annot=True)
plt.title('Correlation Heatmap between RLC, SNT, GNT'+ title_tstamp)
#plt.show()
plt.savefig(dir + 'Correlation_Heatmap')

# return ratio = current value of the cryptocurrency / initial value of the cryptocurrency

returns = close.apply(lambda x: x/x[0])
returns.plot(figsize=(12,6))
plt.ylabel('Return ratio')
plt.xlabel('time')
plt.title('ROI of each Cryptocurrencies in 2019\n return ratio = current value of the cryptocurrency / initial value of the cryptocurrency' + title_tstamp)

plt.savefig(dir + 'ROI_of_each_Cryptocurrencies')

# ### Candlestick Charts Using Plotly (BitCoin)<a id="3-6"></a>
# A candlestick chart (also called Japanese candlestick chart) is a style of financial chart used
#to describe price movements of a security, derivative, or currency.
# Each "candlestick" typically shows one day; so for example a one-month chart may show the 20 trading days as 20 "candlesticks".
# We choose to plot a cancdlestick chart for BitCoin
# since everyone's super curious on whether BitCoin is going to be economic bubble or it's still something that worth to invest in.

increasing_color = '#17BECF'
decreasing_color = '#7F7F7F'
data_plotly = []
layout = {
    'xaxis': {
        'rangeselector': {
            'visible': True
        }
    },
    # Adding a volume bar chart for candlesticks is a good practice usually
    'yaxis': {
        'domain': [0, 0.2],
        'showticklabels': False
    },
    'yaxis2': {
        'domain': [0.2, 0.8]
    },
    'legend': {
        'orientation': 'h',
        'y': 0.9,
        'yanchor': 'bottom'
    },
    'margin': {
        't': 40,
        'b': 40,
        'r': 40,
        'l': 40
    }
}

# Defining main chart
trace0 = go.Candlestick(
    x=rlc.index, open=rlc['open'], high=rlc['high'],
    low=rlc['low'], close=rlc['close'],
    yaxis='y2', name='rlc',
    increasing=dict(line=dict(color=increasing_color)),
    decreasing=dict(line=dict(color=decreasing_color)),
)

data_plotly.append(trace0)

# Adding some range buttons to interact
rangeselector = {
    'visible': True,
    'x': 0,
    'y': 0.8,
    'buttons': [
        {'count': 1, 'label': 'reset', 'step': 'all'},
        {'count': 6, 'label': '6 mo', 'step': 'month', 'stepmode': 'backward'},
        {'count': 3, 'label': '3 mo', 'step': 'month', 'stepmode': 'backward'},
        {'count': 1, 'label': '1 mo', 'step': 'month', 'stepmode': 'backward'},
    ]
}

layout['xaxis'].update(rangeselector=rangeselector)

# Setting volume bar chart colors
colors = []
for i, _ in enumerate(rlc.index):
    if i != 0:
        if rlc['close'].iloc[i] > rlc['close'].iloc[i-1]:
            colors.append(increasing_color)
        else:
            colors.append(decreasing_color)
    else:
        colors.append(decreasing_color)

trace1 = go.Bar(
    x=rlc.index, y=rlc['volume'],
    marker=dict(color=colors),
    yaxis='y', name='Volume'
)

data_plotly.append(trace1)

# Adding Moving Average
def moving_average(interval, window_size=10):
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(interval, window, 'same')

trace2 = go.Scatter(
    x=rlc.index[5:-5], y=moving_average(rlc['close'])[5:-5],
    yaxis='y2', name='Moving Average',
    line=dict(width=1)
)

data_plotly.append(trace2)

# Adding boilinger bands
def bollinger_bands(price, window_size=10, num_of_std=5):
    rolling_mean = price.rolling(10).mean()
    rolling_std = price.rolling(10).std()
    upper_band = rolling_mean + (rolling_std * 5)
    lower_band = rolling_mean - (rolling_std * 5)
    return upper_band, lower_band

bb_upper, bb_lower = bollinger_bands(rlc['close'])

trace3 = go.Scatter(
    x=rlc.index, y=bb_upper,
    yaxis='y2', line=dict(width=1),
    marker=dict(color='#ccc'), hoverinfo='none',
    name='Bollinger Bands',
    legendgroup='Bollinger Bands'
)
data_plotly.append(trace3)

trace4 = go.Scatter(
    x=rlc.index, y=bb_lower,
    yaxis='y2', line=dict(width=1),
    marker=dict(color='#ccc'), hoverinfo='none',
    name='Bollinger Bands', showlegend=False,
    legendgroup='Bollinger Bands'
)
data_plotly.append(trace4)
fig = go.Figure(data=data_plotly, layout=layout)
py.iplot(fig, filename='rlc-candlestick')
io.orca.config
io.orca.status
io.write_image(fig, dir + 'cancdlestick_chart_for_rlc.png')

# How to read the candlestick chart:
# <img src='http://www.greenboxmarkets.com/wp-content/uploads/2016/08/japanese-candlesticks-chart-introduction-1.jpg'>
# 1. Blue colored candlestick means if the price of bitcoin is increasing for that day compares to previous day, while the grey candlestick means the price is decreasing.
# 2. The red trend line is indicating the moving average of 10 days.
# 3. Bollinger Bands consist of: an N-period moving average (MA) an upper band at K times an N-period standard deviation above the moving average (MA + Kσ) a lower band at K times an N-period standard deviation below the moving average (MA − Kσ).
# 4. The bottom chart is the time range.
# 5. Each candlestick gives 4 daily values: open, high, low, and close. (If there's less value, that means two or more of the value is the same)
# 6. Based on the chart, and based onthe last candlestick, we can infer from its large body but short wick that the price might keep dropping after February 22nd.

# ## 4. Building Models - Predicting Price for Cryptocurrencies<a id="4"></a>

# ### Prepare Data for Models<a id="4-1"></a>

# I will separate the data set and build model on each cryptocurrencie type.
#
# For data preparation, I will follow below steps:
# 1. remove 'slug', 'name', 'symbol' and ''ranknow' from data set
# 2. move all 'daily_avg' values 30 lines up in our last cell(one month lag) and define a new column, 'daily_avg_After_Month'
# 3. choose 'daily_avg_After_Month' as target and all other variables as predictors
# 4. create train and test data by splitting the data set to 80-20
# 5. create 'X_forecast' using all predictors with NA 'daily_avg_After_Month' (to predict price in next 30 days)

# In[29]:


# droping 'slug' and 'name' as we can just use 'symbol', and droping 'ranknow'.
data=data.drop(['slug', 'name', 'ranknow'], axis=1)

# Bitcoin (BTC)
BTC = data[data.symbol == 'BTC'].copy()
BTC['daily_avg_After_Month']=BTC['daily_avg'].shift(-30)
X_BTC = BTC.dropna().drop(['daily_avg_After_Month','symbol','daily_avg'], axis=1)
y_BTC = BTC.dropna()['daily_avg_After_Month']
X_train_BTC, X_test_BTC, y_train_BTC, y_test_BTC = train_test_split(X_BTC, y_BTC, test_size=0.2, random_state=43)
X_forecast_BTC =  BTC.tail(30).drop(['daily_avg_After_Month','symbol','daily_avg'], axis=1)

# rlc
RLC = data[data.symbol == 'RLC'].copy()
RLC['daily_avg_After_Month']=RLC['daily_avg'].shift(-30)
X_RLC = RLC.dropna().drop(['daily_avg_After_Month','symbol','daily_avg'], axis=1)
y_RLC = RLC.dropna()['daily_avg_After_Month']
X_train_RLC, X_test_RLC, y_train_RLC, y_test_RLC = train_test_split(X_RLC, y_RLC, test_size=0.2, random_state=43)
X_forecast_RLC =  RLC.tail(30).drop(['daily_avg_After_Month','symbol','daily_avg'], axis=1)

# gnt
GNT = data[data.symbol == 'GNT'].copy()
GNT['daily_avg_After_Month']=GNT['daily_avg'].shift(-30)
X_GNT = GNT.dropna().drop(['daily_avg_After_Month','symbol','daily_avg'], axis=1)
y_GNT = GNT.dropna()['daily_avg_After_Month']
X_train_GNT, X_test_GNT, y_train_GNT, y_test_GNT = train_test_split(X_GNT, y_GNT, test_size=0.2, random_state=43)
X_forecast_GNT =  GNT.tail(30).drop(['daily_avg_After_Month','symbol','daily_avg'], axis=1)

# snm
SNM = data[data.symbol == 'SNM'].copy()
SNM['daily_avg_After_Month']=SNM['daily_avg'].shift(-30)
X_SNM = SNM.dropna().drop(['daily_avg_After_Month','symbol','daily_avg'], axis=1)
y_SNM = SNM.dropna()['daily_avg_After_Month']
X_train_SNM, X_test_SNM, y_train_SNM, y_test_SNM = train_test_split(X_SNM, y_SNM, test_size=0.2, random_state=43)
X_forecast_SNM =  SNM.tail(30).drop(['daily_avg_After_Month','symbol','daily_avg'], axis=1)

# ### Applying Machine Learning Models<a id="4-2"></a>

# define regression function
def regression(X_train, X_test, y_train, y_test):
    Regressor = {
        'Random Forest Regressor': RandomForestRegressor(n_estimators=200),
        'Gradient Boosting Regressor': GradientBoostingRegressor(n_estimators=500),
        'ExtraTrees Regressor': ExtraTreesRegressor(n_estimators=500, min_samples_split=5),
        'Bayesian Ridge': BayesianRidge(),
        'Elastic Net CV': ElasticNetCV()
    }

    for name, clf in Regressor.items():
        print(name)
        clf.fit(X_train, y_train)

        print('R2: {' + str(r2_score(y_test, clf.predict(X_test))) + '}')
        print('MAE: {' + str(mean_absolute_error(y_test, clf.predict(X_test))) + '}')
        print('MSE: {' + str(mean_squared_error(y_test, clf.predict(X_test))) + '}')

# Bitcoin (BTC)
print('Bitcoin (BTC):')
regression(X_train_BTC, X_test_BTC, y_train_BTC, y_test_BTC)

# Bitcoin (BTC)
print('iExec (RLC):')
regression(X_train_RLC, X_test_RLC, y_train_RLC, y_test_RLC)

# GNT  (GNT)
print('GNT (GNT):')
regression(X_train_GNT, X_test_GNT, y_train_GNT, y_test_GNT)

# SNM
print('sonm (SNM):')
regression(X_train_SNM, X_test_SNM, y_train_SNM, y_test_SNM)

# As for all the five algorithms, I will end up taking Extra Trees Regressor for all cryptos
# but XRP and LTC, since this algorithm perform better than all other algorithms in all indicators(R2, MAE and MSE).
# For XRP and LTC, the Random Forest Regressor perform distinctly better than all other algorithms.

# ### Prices Prediction<a id="4-3"></a>

# define prediction function
def prediction(name, X, y, X_forecast):
    if name in ['XRP', 'LTC']:
        model = RandomForestRegressor(n_estimators=200)
    else:
        model = ExtraTreesRegressor(n_estimators=500, min_samples_split=5)
    model.fit(X, y)
    target = model.predict(X_forecast)
    return target

# calculate forecasted prices for next 30 days
forecasted_BTC = prediction('BTC', X_BTC, y_BTC, X_forecast_BTC)
forecasted_RLC = prediction('RLC', X_RLC, y_RLC, X_forecast_RLC)
forecasted_GNT = prediction('GNT', X_GNT, y_GNT, X_forecast_GNT)
forecasted_SNM = prediction('SNM', X_SNM, y_SNM, X_forecast_SNM)

# define index for next 30 days
last_date=data.iloc[-1].name
modified_date = last_date + dt.timedelta(days=1)
new_date = pd.date_range(modified_date,periods=30,freq='D')

# assign prediction to newly defined index
forecasted_BTC = pd.DataFrame(forecasted_BTC, columns=['daily_avg'], index=new_date)
forecasted_RLC = pd.DataFrame(forecasted_RLC, columns=['daily_avg'], index=new_date)
forecasted_GNT = pd.DataFrame(forecasted_GNT, columns=['daily_avg'], index=new_date)
forecasted_SNM = pd.DataFrame(forecasted_SNM, columns=['daily_avg'], index=new_date)

# combine historical price and predicted price
bitcoin = pd.concat([data[data['symbol']=='BTC'][['daily_avg']], forecasted_BTC])
rlc = pd.concat([data[data['symbol']=='RLC'][['daily_avg']], forecasted_RLC])
snm = pd.concat([data[data['symbol']=='SNM'][['daily_avg']], forecasted_SNM])
gnt = pd.concat([data[data['symbol']=='GNT'][['daily_avg']], forecasted_GNT])

# Looking at the short-term forcasted trend in next month,

plt.figure(figsize=(15,8))
(bitcoin[:-30]['daily_avg']).plot(label='Historical Price')
(bitcoin[-31:]['daily_avg']).plot(label='Predicted Price')

plt.xlabel('Time')
plt.ylabel('Price in USD')
plt.title('Prediction on Daily Average Price of Bitcoin' + title_tstamp)
plt.legend()
#plt.show()
plt.savefig(dir + 'Prediction_on_Daily_Average_Price_of_Bitcoin')

#rlc
plt.figure(figsize=(15,8))
(rlc[:-30]['daily_avg']).plot(label='Historical Price')
(rlc[-31:]['daily_avg']).plot(label='Predicted Price')

plt.xlabel('Time')
plt.ylabel('Price in USD')
plt.title('Prediction on Daily Average Price of RLC' + title_tstamp)
plt.legend()
#plt.show()
plt.savefig(dir + 'Prediction_on_Daily_Average_Price_of_RLC')

#

plt.figure(figsize=(15,8))
(gnt[:-30]['daily_avg']).plot(label='Historical Price')
(gnt[-31:]['daily_avg']).plot(label='Predicted Price')

plt.xlabel('Time')
plt.ylabel('Price in USD')
plt.title('Prediction on Daily Average Price of GNT' + title_tstamp)
plt.legend()
#plt.show()
plt.savefig(dir + 'Prediction_on_Daily_Average_Price_of_GNT')

#

plt.figure(figsize=(15,8))
(snm[:-30]['daily_avg']).plot(label='Historical Price')
(snm[-31:]['daily_avg']).plot(label='Predicted Price')

plt.xlabel('Time')
plt.ylabel('Price in USD')
plt.title('Prediction on Daily Average Price of SNM' + title_tstamp)
plt.legend()
#plt.show()
plt.savefig(dir + 'Prediction_on_Daily_Average_Price_of_SNM')
# ## 6. Future Work<a id="6"></a>

# - Some statistical methods for time series forecasting could also be applied such as ARIMA.
# - More predictors could be collected to make a better prediction.
# - Algorithm parameters could be better tuned by using GridSearch or similar techniques.
# - The model will be keep improving as the data volumn become larger.

# ## 7. Reference<a id="7"></a>

# - https://www.kaggle.com/jessevent/all-crypto-currencies/data
# - https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python
# - http://www.businessinsider.com/invest-cryptocurrency-blockchain-technology-2017-8

# ***
