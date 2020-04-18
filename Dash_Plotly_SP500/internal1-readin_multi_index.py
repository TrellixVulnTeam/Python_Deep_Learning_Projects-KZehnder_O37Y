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
import bs4 as bs
import requests
import numpy as np
style.use('ggplot')

df = pd.read_csv('testDf.csv', index_col=[0], header=[0,1,2])
df.head()
