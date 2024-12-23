import streamlit as st
import pandas as pd

def render_ui():
    tickers = st.text_input("티커 입력 (쉼표로 구분)", "AAPL,BTC-USD").split(",")
    tickers = [ticker.strip() for ticker in tickers if ticker.strip()]
    start_date = st.date_input("시작 날짜", pd.to_datetime("2020-01-01"))
    end_date = st.date_input("종료 날짜", pd.to_datetime("2023-01-01"))

    selected_strategy = st.selectbox("전략 선택", ["Super Trend", "Bollinger Band", "Trailing Stop"])

    strategy_params = {}
    if selected_strategy == "Super Trend":
        strategy_params['atr_period'] = st.slider("ATR 기간", 5, 50, 14)
        strategy_params['multiplier'] = st.slider("Multiplier", 1.0, 5.0, 3.0)
    elif selected_strategy == "Bollinger Band":
        strategy_params['window'] = st.slider("볼린저 밴드 기간", 10, 100, 20)
        strategy_params['std_dev'] = st.slider("표준편차 계수", 1.0, 3.0, 2.0)
    else:
        strategy_params['atr_window'] = st.slider("ATR 기간", 5, 50, 14)
        strategy_params['atr_mult'] = st.slider("ATR 계수", 1.0, 5.0, 2.0)
    
    return tickers, start_date, end_date, selected_strategy, strategy_params
