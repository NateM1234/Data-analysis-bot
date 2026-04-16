import yfinance as yf
import pandas as pd
from datetime import datetime
from data.fetcher import fetch_user_data


ticker = input("Input ticker (e.g. MSFT): ")
df = fetch_user_data(ticker)

if df is not None:
    print(df.head())
