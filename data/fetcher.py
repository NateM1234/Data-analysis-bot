import yfinance as yf
import pandas as pd

def fetch_user_data(ticker, period="6mo"):
    data = yf.download(ticker, period=period, auto_adjust=True, progress=False)

    if data.empty:
        print('Option not identified')
        return None

    return data



