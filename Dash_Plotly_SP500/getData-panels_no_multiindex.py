from pymongo import MongoClient
import pymongo
import quandl
import datetime as dt
from bson.objectid import ObjectId
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
#from matplotlib.finance import candlestick_ohlc
from matplotlib import style
import pandas_datareader.data as web
import pandas as pd
import pprint
import numpy as np
style.use('ggplot')

# initialize variables
start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()

# get data
df = web.DataReader('AMD','yahoo',start,end)
df.head()
df.isnull().sum()
df.isnull().sum().sum()
df.select_dtypes(include='number').head()
# df.count() # count tells you number of non missing values
df.count()
