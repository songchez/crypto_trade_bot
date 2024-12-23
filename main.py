import streamlit as st
from components.ui import render_ui
from components.strategies import execute_strategy
from components.data_fetcher import fetch_data

def main():
    st.title("추세추종 전략 및 다중 티커 추세 감지")
    
    # 사용자 UI 렌더링
    tickers, start_date, end_date, selected_strategy, strategy_params = render_ui()
    
    if st.button("데이터 다운로드 및 전략 실행"):
        # 데이터 다운로드
        data_dict, successful_tickers, failed_tickers = fetch_data(tickers, start_date, end_date)
        
        if not successful_tickers:
            st.error("유효한 데이터를 가져올 수 없습니다.")
            return
        
        st.write(f"성공한 티커: {', '.join(successful_tickers)}")
        st.write(f"실패한 티커: {', '.join(failed_tickers)}")
        
        for ticker in successful_tickers:
            ohlcv_data = data_dict[ticker]
            execute_strategy(ticker, ohlcv_data, selected_strategy, strategy_params)

if __name__ == "__main__":
    main()