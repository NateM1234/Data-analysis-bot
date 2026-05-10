from data.fetcher import fetch_user_data, clean_data
from analysis.indicators import add_indicators, generate_signals, apply_stop_loss, position_sizing

def generate_advice(data, ticker):
    if data is None:
        return None
    
    values = {}

    last = data.iloc[-1]

    if (last['RSI'] > 75 ):
        values['rsi_advice'] = "Overbought — momentum may be fading"

    elif (last['RSI'] < 30 ):
        values['rsi_advice'] = "Oversold"
    else:
        values['rsi_advice'] = "Neutral momentum"


    values['ticker'] = ticker
    values['price']  = last['Close']    
    values['signal'] = last['Signal']

    if (last['SMA_20'] > last['SMA_50']):
        values['trend_advice'] = "Uptrend"

    else:
        values['trend_advice'] = "Downtrend"

    if last['Volatility'] > last['Volatility_MA30']:
        values['volatility_advice'] = "High volatility - reduce position size"
    else:
        values['volatility_advice'] = "Low volatility - safer conditions"

    return values