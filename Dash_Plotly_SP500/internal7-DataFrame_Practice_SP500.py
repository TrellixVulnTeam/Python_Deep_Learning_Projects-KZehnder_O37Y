from pymongo import MongoClient
import pymongo
import quandl
import requests
import bs4 as bs
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
#from matplotlib.finance import candlestick_ohlc
from matplotlib import style
import pandas_datareader.data as web
import pandas as pd
import pprint
import numpy as np
import gridfs
import math
from io import StringIO
import os
import io
style.use('ggplot')
from gridfs import GridFS
from datetime import datetime
# Change the size of plots

def get_clean_data(filename):
    clean_df = pd.read_csv(filename)
    clean_df['Date'] = pd.to_datetime(clean_df['Date'])
    del clean_df['Unnamed: 0']
    clean_df.index = clean_df['Date']
    del clean_df['Date']

    return clean_df

filename = 'readable_SP500_data.csv'
df = get_clean_data(filename)
############################################################################################################
mask1 = (df['Stock'] == 'NWS')
mask2 = (df.index > '2015, 01, 01') & (df.index < '2016, 01, 01')
mask3 = (df['Adj Close'] > int(13))

#dff = df.loc[mask1 & mask2 & mask3][['Adj Close']]
# dff = df.loc[mask1 & mask2 & mask3, ['Adj Close']]

dff.plot(grid=True)
