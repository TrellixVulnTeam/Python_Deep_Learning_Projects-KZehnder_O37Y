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

#
start = dt.datetime(2015, 1, 1)
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

testDf = save_sp500_tickers()
print(testDf.head()
)# sent to mongo.......dash will grab from mongo
print('[INFO] Saving SP500 data to CSV at {}'.format(dt.datetime.now()))
testDf.to_csv('readable_SP500_data.csv')
