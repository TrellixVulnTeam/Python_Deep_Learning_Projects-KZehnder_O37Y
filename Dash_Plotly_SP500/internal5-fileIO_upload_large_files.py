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
import io
from gridfs import GridFS
style.use('ggplot')


def insert_document_gridfs(fs, filename):

    """ Function to insert a document into a MongoDB database and return the document's id.
    """
    with io.FileIO(filename, 'r') as fileObject:
        objectID = fs.put(fileObject)

    return objectID

# begin main code
df = pd.read_csv('smallSP500.csv')
df.head(2)
# insert the get sp_500_data function here...then save to csv...
# then
###################################################
# setup client
client = pymongo.MongoClient("mongodb+srv://raspi3eee:Canseco1345@cluster0-gcyzd.gcp.mongodb.net/test?retryWrites=true&w=majority")

 # database?
db = client['sample_database']
#company = db['ShitsGiggs Company']
fs = gridfs.GridFS(db)

# myFile = open('smallSP500.csv', 'r')
# fid = fs.put(myFile, filename='myFile')
# df.reset_index(inplace=True)
# data_dict = df.to_dict('records')
filename_in = 'smallSP500.csv'
input_id = insert_document_gridfs(fs, filename_in)
print('input id', input_id)
