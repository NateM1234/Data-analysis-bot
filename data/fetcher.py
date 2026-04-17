import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_user_data(ticker, period="6mo"):
    data = yf.download(ticker, period=period, auto_adjust=True, progress=False)

    if data.empty:
        print('Option not identified')
        return None
    data.columns = data.columns.droplevel(1)
    return data

def clean_data(data):
    if data is None:
        return None

    data = data.dropna(subset=['Close', 'High', 'Low', 'Volume'])
    data = data[['Close', 'High', 'Low', 'Volume']]
    data = data.sort_index()

    return data


