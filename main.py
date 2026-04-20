import yfinance as yf
import pandas as pd
from datetime import datetime
from data.fetcher import fetch_user_data, clean_data
from analysis.indicators import add_indicators, generate_signals, apply_stop_loss, position_sizing

ticker = input("Input ticker (e.g. MSFT): ")
raw = fetch_user_data(ticker)
clean = clean_data(raw)
data = add_indicators(clean)
data = generate_signals(data)

print(data[['Close', 'RSI', 'SMA_20', 'SMA_50', 'Signal']].tail(10))

if clean is not None:
    print(clean.head())
    print(clean.shape)

