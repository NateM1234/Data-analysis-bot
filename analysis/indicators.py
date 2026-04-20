import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def add_indicators(data):
    if data is None:
        return None
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()

    delta = data['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100/ (1 + rs))

    #volume
    data['Volume_MA20'] = data['Volume'].rolling(20).mean()


    #volatility
    daily_return = data['Close'].pct_change()
    data['Volatility'] = daily_return.rolling(20).std() * (252 ** 0.5)
    data['Volatility_MA30'] = data['Volatility'].rolling(30).mean()

    return data

def generate_signals(data):
    if data is None:
        return None
    
    data['Signal'] = 'hold'    
    for i in range(len(data)):
        if (
            data['RSI'].iloc[i] < 60 and 
            data['RSI'].iloc[i] > 40 and 
            data['SMA_20'].iloc[i] > data['SMA_50'].iloc[i] and
            data['Volume'].iloc[i] > data['Volume_MA20'].iloc[i] and
            data['Volatility'].iloc[i] < data['Volatility_MA30'].iloc[i]

        ):
            data.at[data.index[i], 'Signal'] = 'Buy'

        elif (
            data['RSI'].iloc[i] > 75 and  
            data['SMA_20'].iloc[i] < data['SMA_50'].iloc[i]

        ):
            data.at[data.index[i], 'Signal'] = 'Sell'

    return data


def apply_stop_loss(entry_price, current_price, threshold=0.07):
    pct_drop = (entry_price - current_price) / entry_price

    return pct_drop >= threshold
   

def position_sizing(capital, volatility, risk_pct=0.02):

    
    
    if volatility == 0:
        return 0
    risk_amount = capital * risk_pct
    
    position_size = risk_amount / volatility
    
    return position_size

