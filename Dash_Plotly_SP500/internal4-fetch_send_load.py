#smallSP500import pandas as pd
import pymongo
import json
import os
from pymongo import MongoClient
import pymongo
import quandl
import requests
import bs4 as bs
from io import StringIO
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
import os
import io
from io import BytesIO
from bson import ObjectId
from gridfs import GridFS
style.use('ggplot')


def insert_document_gridfs(fs, filename):

    """ Function to insert a document into a MongoDB database and return the document's id.
    """
    with io.FileIO(filename, 'r') as fileObject:
        objectID = fs.put(fileObject)
        if objectID:
            print('[INFO] Successfull upload...id_={}'.format(objectID))
        else:
            print('[INFO] Error...')

    return objectID

def save_sp500_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})

    data = None
    stocks = []
    industries = []

    for row in table.findAll('tr')[1:]:
            stock = row.findAll('td')[0].text
            industry = row.findAll('td')[4].text

            stocks.append(stock)
            industries.append(industry)

    stocks = list(map(lambda s: s.strip(), stocks))
    industries = list(map(lambda s: s.strip(), industries))

    for i, (stock, industry) in enumerate(zip(stocks[:10], industries[:10])):
        if i % 10 == 0:
            print(['[INFO] progress getting stock {} of {}'.format(i, len(stocks))])

        try:
            stock_data = web.DataReader(stock, 'yahoo', start, end)
            stock_data.insert(0, 'Stock', stock)
            stock_data.insert(1, 'Industry', industry)
            print(stock_data.head())
            if data is None:
                data = stock_data
            else:
                data = pd.concat([data, stock_data])

        except Exception as e:
            #pass
            print('error with stock = {}'.format(stock))

    return data

start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()

mng_client = pymongo.MongoClient("mongodb+srv://raspi3eee:Canseco1345@cluster0-gcyzd.gcp.mongodb.net/test?retryWrites=true&w=majority")

mng_db = mng_client['GIZA']
#db_cm = mng_db[collection_name]

# NOTE: NEED TO ADD GRID FS!!!
fs = gridfs.GridFS(mng_db)

store_string = 'MINI_SP500.csv'
#data = save_sp500_tickers() # can add into function the ability to send to csv there
#data.to_csv(store_string)
#data = pd.read_csv('smallSP500.csv')

# store_string = store_string
print('[INFO] now grabbing csv from local file and storing to mongodb...')
#ob = insert_document_gridfs(fs, store_string)
#print(ob)
# with io.FileIO(filename, 'r') as fileObject:
#     objectID = fs.put(fileObject)
#     print(objectID)


# with io.FileIO('MINI_SP500.csv', 'wb') as fileObject:
#     #print('tyoe fileObject = {}'.format(type(fileObject)))
#     fileObject.write(fo.read())

#fo.read()
#pd.read_csv('MINI_SP500.csv')


dir(fs)
x = fs.find_one()
type(x)
# copy and pasted this oid number directly from the mongodb database
oid = '5e969bda8b34f2235ad8836b'
file = fs.get(ObjectId(oid))
dir(file)
s = StringIO(file.read().decode())
dir(s)
s
