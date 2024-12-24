import streamlit as st
import pandas as pd
import vectorbt as vbt
from strategies.supertrend import supertrend
from strategies.bollinger_band import bollinger_band_strategy
from strategies.trailing_stop import trailing_stop_strategy
from strategies.rsi_macd_sto import rsi_macd_stochastic_strategy



# 전략들과 각 파라미터를 모아서 직접 백테스팅
def execute_strategy(ticker, ohlcv_data, strategy_name, params, fee, cash):
    close = ohlcv_data['Close']
    
    if strategy_name == "Super Trend":
        entries, exits = supertrend(ohlcv_data, params['atr_period'], params['multiplier'])
    elif strategy_name =="Rsi&Macd$Sto":
        entries, exits = rsi_macd_stochastic_strategy(ohlcv_data,  params['rsi_period'], params['stochastic_k'])
    elif strategy_name == "Bollinger Band":
        entries, exits = bollinger_band_strategy(close, params['window'], params['std_dev'])
    else:
        entries, exits = trailing_stop_strategy(close, params['atr_window'], params['atr_mult'])
    
    portfolio = vbt.Portfolio.from_signals(close, entries, exits, init_cash=cash, fees=fee)
    st.write(f"### {ticker} 백테스팅 결과")

    total_profit_value = portfolio.total_profit().sum() if isinstance(portfolio.total_profit(), pd.Series) else portfolio.total_profit()
    final_value = cash + total_profit_value  # 총 자본 계산
    
    if total_profit_value > 0:
        st.write(f"손익: :red[{total_profit_value:,.0f} 원]")
    else:
        st.write(f"손익: :blue[{total_profit_value:,.0f} 원]")
    st.write(f"최종 자본: {final_value:,.0f} 원")
    st.line_chart(portfolio.value())
