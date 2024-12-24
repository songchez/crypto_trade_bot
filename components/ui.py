import streamlit as st
import pandas as pd

def render_ui():
    tickers = st.text_input("티커 입력 (쉼표로 구분)", "AAPL,BTC-USD").split(",")
    tickers = [ticker.strip() for ticker in tickers if ticker.strip()]

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("시작 날짜", pd.to_datetime("2020-01-01"))
    with col2:
        end_date = st.date_input("종료 날짜", pd.to_datetime("2024-12-20"))

    interval = st.radio(
        "원하는 기준봉을 선택하세요:",
        options=['5m', '15m', '1h', '4h', '1d', '1wk'],
        index=3,
        horizontal=True,
    )

    # 기준봉별 최대 허용 기간 설정
    interval_limits = {
        '5m': 60,  # 최대 60일
        '15m': 60, # 최대 60일
        '1h': 730, # 최대 730일
        '4h': 730, # 최대 730일
        '1d': None, # 제한 없음
        '1wk': None # 제한 없음
    }

    # 날짜 차이 계산
    date_diff = (end_date - start_date).days

    # 조건 검증 및 메시지 출력
    max_days = interval_limits.get(interval)
    if max_days is not None and date_diff > max_days:
        st.error(f"현 기준봉('{interval}')에서는 최대 {max_days}일까지만 선택 가능합니다.")

    # 전략 선택 및 매개변수 설정
    selected_strategy = st.selectbox("전략 선택", ["Super Trend", "Rsi&Macd$Sto", "Bollinger Band", "Trailing Stop"])
    strategy_params = {}
    
    if selected_strategy == "Super Trend":
        strategy_params['atr_period'] = st.slider("ATR 기간", 5, 50, 14)
        strategy_params['multiplier'] = st.slider("Multiplier", 1.0, 5.0, 3.0)
    elif selected_strategy == "Rsi&Macd$Sto":
        strategy_params['rsi_period'] = st.slider("RSI범위", 10, 30, 14)
        strategy_params['stochastic_k'] = st.slider("스토캐스틱K", 10, 30, 14)
    elif selected_strategy == "Bollinger Band":
        strategy_params['window'] = st.slider("볼린저 밴드 기간", 10, 100, 20)
        strategy_params['std_dev'] = st.slider("표준편차 계수", 1.0, 3.0, 2.0)
    else:
        strategy_params['atr_window'] = st.slider("ATR 기간", 5, 50, 14)
        strategy_params['atr_mult'] = st.slider("ATR 계수", 1.0, 5.0, 2.0)
    
    return tickers, start_date, end_date, selected_strategy, strategy_params, interval