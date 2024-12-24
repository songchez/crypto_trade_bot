
import streamlit as st
import streamlit.components.v1 as components
from components.ui import render_ui
from components.strategies import execute_strategy
from components.data_fetcher import fetch_data


st.set_page_config(
    page_title="TBOT1.0S | HOME",
    page_icon="🐢",
)

def main():
    st.title("🐢 터틀 백테스트봇S 1.0")
    
    # 사용자 UI 렌더링
    tickers, start_date, end_date, selected_strategy, strategy_params, interval, fee, cash = render_ui()
    
    if st.button("데이터 다운로드 및 전략 실행"):
        # 데이터 다운로드
        data_dict, successful_tickers, failed_tickers = fetch_data(tickers, start_date, end_date, interval)
        
        if not successful_tickers:
            st.error("유효한 데이터를 가져올 수 없습니다.")
            return
        
        st.write(f"성공한 티커: {', '.join(successful_tickers)}")
        st.write(f"실패한 티커: {', '.join(failed_tickers)}")
        
        for ticker in successful_tickers:
            ohlcv_data = data_dict[ticker]
            execute_strategy(ticker, ohlcv_data, selected_strategy, strategy_params, fee, cash)

        # buy_me_a_coffee 코드
        buy_me_a_coffee_button = """
        <a href="https://www.buymeacoffee.com/tama4840X" target="_blank">
        <img src="https://img.buymeacoffee.com/button-api/?text=Buy me a Coffee&emoji=&slug=tama4840X&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" /></a>
        """
        st.write(":red[⬇ 개발자에게 커피 한 잔 사주기♡ ⬇]")
        components.html(buy_me_a_coffee_button, height=70)

if __name__ == "__main__":
    main()