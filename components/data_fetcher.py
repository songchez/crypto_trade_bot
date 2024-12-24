import yfinance as yf
import streamlit as st

@st.cache_data
def fetch_data(tickers, start_date, end_date, interval='1d'):
    data_dict = {}
    successful_tickers = []
    failed_tickers = []

    for ticker in tickers:
        try:
            if interval == '4h':
                df = yf.download(ticker.strip(), start=start_date, end=end_date, interval='1h')
                data = df.resample('4H').agg({
                    'Open': 'first',
                    'High': 'max',
                    'Low': 'min',
                    'Close': 'last',
                    'Volume': 'sum'
                })
            else:
                data = yf.download(ticker.strip(), start=start_date, end=end_date, interval=interval)

            print(data)
            if not data.empty:
                data_dict[ticker.strip()] = data
                successful_tickers.append(ticker.strip())
            else:
                failed_tickers.append(ticker.strip())
        except Exception as e:
            failed_tickers.append(ticker.strip())
            print(f"티커 {ticker} 다운로드 중 오류 발생: {e}")
    return data_dict, successful_tickers, failed_tickers
