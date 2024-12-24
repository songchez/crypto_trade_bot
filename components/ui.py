import streamlit as st
import pandas as pd

# 웹 UI 전체
def render_ui():
    col1, col2 = st.columns(2)
    with col1:
        tickers = st.text_input("티커 입력 (쉼표로 구분)", "AAPL,BTC-USD").split(",")
        tickers = [ticker.strip() for ticker in tickers if ticker.strip()]
    with col2:
        cash = st.number_input("자본금(원)",None,100000000000,300000,100000)

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("시작 날짜", pd.to_datetime("2023-01-01"))
    with col2:
        end_date = st.date_input("종료 날짜", pd.to_datetime("today"))

    col1, col2 = st.columns(2)
    with col1:
        interval_mapping = {
            '5분': '5m',
            '15분': '15m',
            '1시간': '1h',
            '4시간': '4h',
            '1일': '1d',
            '1주': '1wk'
        }
        interval_korean = st.radio("원하는 기준봉을 선택하세요:", options=list(interval_mapping.keys()),index=3, horizontal=True)
        interval = interval_mapping[interval_korean]
    with col2:
        fee = st.number_input("수수료율(%)", 0.001, 15.001, 0.051, 0.01, "%.3f")

    # 기준봉별 최대 허용 기간 설정
    interval_limits = {
        '5m': 60,  # 최대 60일
        '15m': 60, # 최대 60일
        '1h': 730, # 최대 730일
        '4h': 730, # 최대 730일
        '1d': None, # 제한 없음
        '1wk': None # 제한 없음
    }

    # 날짜 제한 자동 적용
    max_days = interval_limits.get(interval)
    if max_days is not None:
        default_start_date = pd.to_datetime("today") - pd.Timedelta(days=max_days)
        if (end_date - start_date).days > max_days:
            st.warning(f"현 기준봉('{interval_korean}')에서는 최대 {max_days}일까지만 선택 가능합니다. "
            f"시작 날짜를 {default_start_date.date()}안쪽으로 조정해주세요")

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

    return tickers, start_date, end_date, selected_strategy, strategy_params, interval, fee, cash