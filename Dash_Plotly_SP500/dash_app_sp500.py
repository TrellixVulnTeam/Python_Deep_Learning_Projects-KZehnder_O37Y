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
import dash_table
import numpy as np
import gridfs
import math
from io import StringIO
import os
import io
from gridfs import GridFS
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

style.use('ggplot')
##########################################################
def get_clean_data(filename):
    clean_df = pd.read_csv(filename)
    clean_df['Date'] = pd.to_datetime(clean_df['Date'])
    #del clean_df['Unnamed: 0']
    clean_df.index = clean_df['Date']
    del clean_df['Date']

    return clean_df

df = get_clean_data('readable_SP500_data.csv')
#########################################################
app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='my-id-input', value='NWS', type='text'),
    #html.Div(id='my-div-output')])
    html.Div(id='basic-graph-container'),
    html.H4(children='Stock Data'),
    html.Div(id='table-container')
    ])

@app.callback(
    Output(component_id='basic-graph-container', component_property='children'), # why can't figure be used here? B/c graph compn
    [Input(component_id='my-id-input', component_property='value')]
)
def update_output_div(input_value):
    dff = df[df['Stock'] == input_value]['Adj Close']

    return dcc.Graph(
        figure={
            'data': [
                {'x': dff.index, 'y': dff.values, 'type': 'line'},
            ],
            'layout': {
                'title': input_value }
        })


@app.callback(
    Output(component_id='table-container', component_property='children'), # why can't figure be used here? B/c graph compn
    [Input(component_id='my-id-input', component_property='value')]
)
def generate_table(selected_stock):
    #dates = df.copy().reset_index(inplace=True)
    #dates = dates['Date']
    dff = df.copy()
    dff = df[df['Stock'] == selected_stock]
    dff.reset_index(inplace=True)
    print(dff.head())
    #dff.insert(0, 'Dates', dates)
    #dff = df.reset_index(inplace=True)
    #dff = dff.iloc[:20, :] # can use this to trim amount of rows of the table to show
    dff = dff.round(2)


    return dash_table.DataTable(
    data=dff.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in dff.columns],
    style_table={
            'maxHeight': '300px',
            'overflowY': 'scroll'
        },
    style_cell_conditional=[
        {'if': {'column_id': 'Industry'},
         'width': '30%'},
    ]
)

if __name__ == '__main__':
    app.run_server()
