import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt



def plot_charts(data, ticker):
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(12, 8))

    ax1.plot(data.index, data['SMA_20'], label='Moving average (20 days)')
    ax1.plot(data.index, data['SMA_50'], label='Moving average (50 days)')
    ax1.plot(data.index, data['Close'], label='Closing price')
    ax1.legend()

    ax2.plot(data.index, data['RSI'], label='RSI average')
    ax2.axhline(y=70, color='red')
    ax2.axhline(y=30, color='green')
    ax2.axhspan(30, 70, alpha=0.1)
    ax2.legend()

    ax1.set_title(ticker)
    plt.tight_layout()
    plt.show()




    
    
