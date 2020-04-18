import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import datetime
import pandas as pd
import numpy as np

df = pd.read_csv('readable_SP500_data.csv')
#df.reset_index(inplace=True)
df.head(2)
df.tail()
dt = '2020, 1, 1'

cond = np.where((df['Industry'] == 'Pharmaceuticals') & (df['Date'] >= dt))
# COND/ AKA np.where is how you get rows that fit certain criteria
x = df.loc[cond]
x.head(2)
#[['Adj Close']]
x2 = x.groupby(['Date','Stock'])[['Adj Close']].max() #doesnt make sense to max for single day but change tomorrow lol
x2
