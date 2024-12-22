"""
main_app.py

Streamlit 기반 메인 애플리케이션
- 개별 종목 백테스트 (Donchian, MA Crossover, Bollinger)
- 다중 티커 추세 전환 감지 (trend_change)
"""

import streamlit as st
import datetime
import backtrader as bt
import yfinance as yf
import matplotlib.pyplot as plt

# 전략 모듈 임포트
from strategies.donchian import DonchianBreakoutStrategy
from strategies.ma_crossover import MovingAverageCrossover
from strategies.bollinger import BollingerBreakoutStrategy

# 추세 감지 모듈
from detectors.trend_change import detect_trend_change

def main():
    st.title("추세 추종 종합 어플리케이션")

    # -------------------
    # 1) 개별 종목 백테스트
    # -------------------
    st.subheader("1) 개별 종목(티커) 백테스트")

    # 사용자 입력
    ticker_symbol = st.text_input("티커 (예: AAPL, BTC-USD, SPY 등)", value="AAPL")
    start_date = st.date_input("시작 날짜", datetime.date(2020,1,1))
    end_date = st.date_input("종료 날짜", datetime.date(2023,1,1))

    strategy_name = st.selectbox("전략 선택", 
                                 ["DonchianBreakout", 
                                  "MovingAverageCrossover",
                                  "BollingerBreakout"])

    if strategy_name == "DonchianBreakout":
        donchian_period = st.number_input("Donchian Period", min_value=1, max_value=200, value=20)
    elif strategy_name == "MovingAverageCrossover":
        fast_period = st.number_input("MA Fast Period", min_value=1, max_value=200, value=20)
        slow_period = st.number_input("MA Slow Period", min_value=1, max_value=300, value=60)
    else:
        bb_period = st.number_input("Bollinger Period", min_value=1, max_value=200, value=20)
        dev_factor = st.number_input("Std Dev Factor", min_value=0.5, max_value=5.0, value=2.0)

    initial_cash = st.number_input("초기 자본", value=100000, step=10000)
    commission = st.number_input("수수료(%)", value=0.1, step=0.05)

    if st.button("백테스트 실행"):
        df = yf.download(ticker_symbol, start=start_date, end=end_date)
        if df.empty:
            st.error("유효한 데이터가 없습니다.")
            return
        
        cerebro = bt.Cerebro()
        data = bt.feeds.PandasData(dataname=df)
        cerebro.adddata(data)

        # 전략 추가
        if strategy_name == "DonchianBreakout":
            cerebro.addstrategy(DonchianBreakoutStrategy, donchian_period=donchian_period)
        elif strategy_name == "MovingAverageCrossover":
            cerebro.addstrategy(MovingAverageCrossover, fast_period=fast_period, slow_period=slow_period)
        else:
            cerebro.addstrategy(BollingerBreakoutStrategy, period=bb_period, devfactor=dev_factor)

        cerebro.broker.setcash(initial_cash)
        cerebro.broker.setcommission(commission=commission/100.0)

        initial_value = cerebro.broker.getvalue()
        st.write(f"초기 포트폴리오 가치: {initial_value:,.2f}")

        cerebro.run()
        final_value = cerebro.broker.getvalue()
        st.write(f"최종 포트폴리오 가치: {final_value:,.2f}")
        st.write(f"수익률: {((final_value - initial_value)/initial_value)*100:,.2f}%")

        # 차트 표시
        fig = cerebro.plot(style='candlestick', iplot=False)[0][0]
        st.pyplot(fig)

    # --------------------------------
    # 2) 다중 티커 추세 전환 감지
    # --------------------------------
    st.subheader("2) 다중 티커 추세 전환 감지")

    default_tickers = "AAPL, BTC-USD, GLD, TLT, SPY"
    user_tickers = st.text_area("티커 목록 (쉼표 구분)", default_tickers)
    
    detect_start = st.date_input("추세 감지 시작 날짜", datetime.date(2023,1,1))
    detect_end = st.date_input("추세 감지 종료 날짜", datetime.date(2023,6,1))
    
    short_ma_period = st.number_input("단기 MA 기간", min_value=1, max_value=200, value=20)
    long_ma_period = st.number_input("장기 MA 기간", min_value=1, max_value=300, value=60)

    if st.button("추세 전환 감지 실행"):
        ticker_list = [t.strip() for t in user_tickers.split(",") if t.strip()]
        results_df = detect_trend_change(
            ticker_list, 
            detect_start, 
            detect_end, 
            short_period=short_ma_period, 
            long_period=long_ma_period
        )
        st.dataframe(results_df)

if __name__ == "__main__":
    main()
