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
from gridfs import GridFS
style.use('ggplot')


# setup client
client = pymongo.MongoClient("mongodb+srv://raspi3eee:Canseco1345@cluster0-gcyzd.gcp.mongodb.net/test?retryWrites=true&w=majority")

 # database?
db = client['abhay_database_large']
#company = db['Large Company']
fs = gridfs.GridFS(db)

# df.reset_index(inplace=True)
# data_dict = df.to_dict('records')

filename = 'readable_SP500_data.csv'
with io.FileIO(filename, 'r') as fileObject:
    objectID = fs.put(fileObject, filename='SP500_document')


# date_inserted = dt.datetime.now()
# meta = {'index': 'smallSP500', 'date_inserted' : date_inserted, 'data' : data_dict}
# ob = fs.put(meta)
# fs.get(ob).read()
# objectID
# find = fs.find_one({'filename' : 'first_document'})
# find.read()
fid = fs.get_last_version(filename='SP500_document')
fid._id
fid_str = fid.read().decode()
type(fid_str)
len(fid_str)

#df = pd.DataFrame([x.split(',') for x in fid_str.split('\n')[1:]], columns=[x for x in fid_str.split('\n')[0].split(',')]
# df

#len(columns)
# columns = [x for x in fid_str.split('\n')[0].split(',')]
# columns
columns_ints = [i for i in range(0, 10)]
columns = ['Date','Stock','Industry','High','Low','Open','Close','Volume','Adj Close','Empty']
#len(columns)
df = pd.DataFrame([x.split(',')[1:] for x in fid_str.split('\n')[1:]], columns=columns)
df.head()
del df['Empty']
df.head()
