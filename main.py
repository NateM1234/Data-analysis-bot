import yfinance as yf
import pandas as pd
from datetime import datetime
from data.fetcher import fetch_user_data, clean_data
from analysis.indicators import add_indicators, generate_signals, apply_stop_loss, position_sizing
from analysis.advice import generate_advice

ticker = input("Input ticker (e.g. MSFT): ")
raw = fetch_user_data(ticker)
clean = clean_data(raw)
data = add_indicators(clean)
data = generate_signals(data)


ti = yf.Ticker(ticker)
news = ti.news()



values = generate_advice(data, ticker)


if clean is not None:
    print(ticker)
    print("\n===============================================================")
    print("                     QUANT TRADING REPORT")
    print("===============================================================")

    print(f"Ticker:              {values['ticker']}")
    print(f"Current Price:       ${values['price']:.2f}")
    print(f"Signal:              {values['signal']}")
    

    print("\n--- Market Analysis ---")
    print(f"Trend Advice:        {values['trend_advice']}")
    print(f"Volatility Advice:   {values['volatility_advice']}")
    print(f"RSI Advice:          {values['rsi_advice']}")


    print(f"News:                {news}")

    print("==============================\n")



