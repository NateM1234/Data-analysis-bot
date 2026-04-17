import yfinance as yf
import pandas as pd
from datetime import datetime
from data.fetcher import fetch_user_data, clean_data


ticker = input("Input ticker (e.g. MSFT): ")
raw = fetch_user_data(ticker)
clean = clean_data(raw)

if clean is not None:
    print(clean.head())
    print(clean.shape)

