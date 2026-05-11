import yfinance as yf
import matplotlib.pyplot as plt

from visualisation.charts import plot_charts
from data.fetcher import fetch_user_data, clean_data
from analysis.indicators import (
    add_indicators,
    generate_signals,
    apply_stop_loss,
    position_sizing
)
from analysis.advice import generate_advice


# MAIN PROGRAM

ticker = input("Input ticker (e.g. MSFT): ").upper()

# Data pipeline
raw = fetch_user_data(ticker)
clean = clean_data(raw)

if clean is not None:

    data = add_indicators(clean)
    data = generate_signals(data)

    # Fetch news
    ti = yf.Ticker(ticker)
    news = ti.news

    # Generate advice dictionary
    values = generate_advice(data, ticker)

    
    print("TERMINAL REPORT")

    print(f"Ticker:              {values['ticker']}")
    print(f"Current Price:       ${values['price']:.2f}")
    print(f"Signal:              {values['signal']}")

    print("\n--- Market Analysis ---")
    print(f"Trend Advice:        {values['trend_advice']}")
    print(f"Volatility Advice:   {values['volatility_advice']}")
    print(f"RSI Advice:          {values['rsi_advice']}")


    print("\n--- Latest News ---")

    if news and len(news) > 0:

        for article in news[:5]:
            title = article.get('content', {}).get('title', 'No title available')
            print(f"- {title}")

    else:
        print("No recent news found.")

    plot_charts(data, ticker)


else:
    print("Failed to fetch or clean stock data.")



