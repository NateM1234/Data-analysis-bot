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
    pass


def apply_stop_loss(data):
    pass

def position_sizing(data, base_size=1.0):
    data['Position_Size'] = base_size / data['Volatility']
    return data

