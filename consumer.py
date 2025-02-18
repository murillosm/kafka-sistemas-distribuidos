
from json import JSONDecoder
import json
from random import choice
import time
import pandas as pd
from kafka import KafkaConsumer

import plotly.graph_objects as go

from util import STOCKS


CONSUMER = KafkaConsumer(f'transaction_{choice(STOCKS)}', bootstrap_servers='localhost:19092', group_id='stock_group', auto_offset_reset='earliest', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

messages = pd.DataFrame(columns=['stock', 'price', 'variation', 'quantity', 'trade_type', 'timestamp'])
messages.set_index('timestamp', inplace=True)
fig : go.Figure = None

flag = True

# TODO: Ajeitar essa parte aqui
def update_candlestick():
    
    global messages
    global flag
    global fig
    
    messages_resampled = messages.resample('1min').agg({'price': ['first', 'max', 'min', 'last']})
    messages_resampled.columns = ['Open', 'High', 'Low', 'Close']
    
    if flag:
        fig = go.Figure(data=[go.Candlestick(
            x=messages_resampled.index,
            open=messages_resampled['Open'],
            high=messages_resampled['High'],
            low=messages_resampled['Low'],
            close=messages_resampled['Close'],
            name="Stock Prices"
        )])
        
        fig.update_layout(
            title="Candlestick Chart - Stock Prices",
            xaxis_title="Time",
            yaxis_title="Price",
            xaxis_rangeslider_visible=False
        )

        flag = False
        fig.show()
    else:
        fig.data = []  # Clear previous data
        fig.add_trace(go.Candlestick(
            x=messages_resampled['date'],
            open=messages_resampled['open'],
            high=messages_resampled['high'],
            low=messages_resampled['low'],
            close=messages_resampled['close'],
            increasing_line_color='green',
            decreasing_line_color='red'
        ))

        #fig.update_layout(title=f'Real-Time Candlestick Chart (Updated at {new_date})')
        fig.update()
    
    time.sleep(1)
    

def consume_transaction():
    
    global messages
    
    for message in CONSUMER:
        
        content = pd.DataFrame([message.value], columns=['stock', 'price', 'variation', 'quantity', 'trade_type', 'timestamp'])
        content['timestamp'] = pd.to_datetime(content['timestamp'])	
    
        messages = pd.concat([messages, content])	
    
        messages.set_index('timestamp', inplace=True)
        
        if len(messages) > 100000:
            messages = messages.tail(100000)

        update_candlestick()
        
if __name__ == '__main__':
    consume_transaction()