import streamlit as st
import pandas as pd
import vectorbt as vbt
from strategies.supertrend import supertrend
from strategies.bollinger_band import bollinger_band_strategy
from strategies.trailing_stop import trailing_stop_strategy
from strategies.rsi_macd_sto import rsi_macd_stochastic_strategy

def execute_strategy(ticker, ohlcv_data, strategy_name, params):
    close = ohlcv_data['Close']
    
    if strategy_name == "Super Trend":
        entries, exits = supertrend(ohlcv_data, params['atr_period'], params['multiplier'])
    elif strategy_name =="Rsi&Macd$Sto":
        entries, exits = rsi_macd_stochastic_strategy(ohlcv_data,  params['rsi_period'], params['stochastic_k'])
    elif strategy_name == "Bollinger Band":
        entries, exits = bollinger_band_strategy(close, params['window'], params['std_dev'])
    else:
        entries, exits = trailing_stop_strategy(close, params['atr_window'], params['atr_mult'])
    
    portfolio = vbt.Portfolio.from_signals(close, entries, exits, init_cash=100_000)
    st.write(f"### {ticker} 백테스팅 결과")

    total_profit_value = portfolio.total_profit().sum() if isinstance(portfolio.total_profit(), pd.Series) else portfolio.total_profit()
    st.write(f"최종 자본: {total_profit_value:,.2f}")
    st.line_chart(portfolio.value())
