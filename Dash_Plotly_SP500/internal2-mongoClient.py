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
import os
style.use('ggplot')
################################################
# this will go in dash to get the data from mongo
from bson.objectid import ObjectId

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})
    #company.find_one({"index": "Sensex"})

##################################################

# setup client
client = pymongo.MongoClient("mongodb+srv://raspi3eee:Canseco1345@cluster0-gcyzd.gcp.mongodb.net/test?retryWrites=true&w=majority")

 # database?
db = client['sample_database']
company = db['Company']
#fs = gridfs.GridFS(db)

# initialize variables
start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()


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

    for i, (stock, industry) in enumerate(zip(stocks, industries)):
        if i % 10 == 0:
            print(['[INFO] progress getting stock {} of {}'.format(i, len(stocks))])

        try:
            stock_data = web.DataReader(stock, 'yahoo', start, end)
            stock_data.insert(0, 'Stock', stock)
            stock_data.insert(1, 'Industry', industry)

            if data is None:
                data = stock_data
            else:
                data = pd.concat([data, stock_data])

        except Exception as e:
            #pass
            print('error with stock = {}'.format(stock))

    return data

df = save_sp500_tickers()
# prepare to load into mongoDB
df.reset_index(inplace=True)
data_dict = df.to_dict('records')

# need to store index with the date that you are entering the results into mongo database
date_inserted = dt.datetime.now()
company.insert_one({'index' : 'SP500_data', 'date_inserted' : date_inserted, 'data' : data_dict})


# date_inserted = dt.datetime.now()
# meta = {'index' : 'SP500_data', 'date_inserted' : date_inserted, 'data' : data_dict}
# company.find_one_and_replace({'index': 'SP500_data'}, meta)
x = company.find_one({'index': 'SP500_data'})
pd.DataFrame.from_dict(x, orient='index')
