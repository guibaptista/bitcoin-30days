!pip install pycoingecko
!pip install plotly
!pip install mplfinance

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc



cg = CoinGeckoAPI()
bitcoin_dados = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

bitcoin_price_dados = bitcoin_dados['prices']
bitcoin_price_dados[0:5]

data = pd.DataFrame(bitcoin_price_dados, columns=['TimeStamp', 'Price'])
data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))

candlestick_data = data.groupby(data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})

fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Price']['first'], 
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'], 
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()
