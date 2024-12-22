"""
trend_change.py

여러 티커(자산군)에 대해 단기/장기 이동평균선
교차로 '추세 전환' 발생을 확인하는 모듈
"""
import yfinance as yf
import pandas as pd
import numpy as np

def detect_trend_change(ticker_list, start_date, end_date, short_period=20, long_period=60):
    """
    - ticker_list: ["AAPL", "BTC-USD", "GLD", ...]
    - start_date, end_date: 분석할 날짜 범위
    - short_period, long_period: 단/장기 이동평균 기간
    - return: pd.DataFrame(columns=["Ticker", "Status", "ShortMA", "LongMA", "Signal"])
    """
    results = []
    
    for ticker in ticker_list:
        try:
            df = yf.download(ticker, start=start_date, end=end_date, progress=False)
            if df.empty:
                # 데이터가 없으면 건너뛰기 or 표시
                results.append({
                    "Ticker": ticker,
                    "Status": "No Data",
                    "ShortMA": np.nan,
                    "LongMA": np.nan,
                    "Signal": None
                })
                continue
            
            # 이동평균 계산
            df["MA_short"] = df["Close"].rolling(short_period).mean()
            df["MA_long"]  = df["Close"].rolling(long_period).mean()
            
            # 직전봉, 현재봉 비교
            if len(df) < 2:
                # 데이터가 너무 짧다면
                results.append({
                    "Ticker": ticker,
                    "Status": "Insufficient Data",
                    "ShortMA": None,
                    "LongMA": None,
                    "Signal": None
                })
                continue

            ma_short_prev = df["MA_short"].iloc[-2]
            ma_short_now  = df["MA_short"].iloc[-1]
            ma_long_prev  = df["MA_long"].iloc[-2]
            ma_long_now   = df["MA_long"].iloc[-1]

            status_text = "No Trend Change"
            signal = None
            
            # 골든크로스(상승 전환)
            if (ma_short_prev <= ma_long_prev) and (ma_short_now > ma_long_now):
                status_text = "Up Trend Change (Golden Cross)"
                signal = "BUY"
            # 데드크로스(하락 전환)
            elif (ma_short_prev >= ma_long_prev) and (ma_short_now < ma_long_now):
                status_text = "Down Trend Change (Death Cross)"
                signal = "SELL"
            
            results.append({
                "Ticker": ticker,
                "Status": status_text,
                "ShortMA": round(ma_short_now, 2) if pd.notnull(ma_short_now) else None,
                "LongMA": round(ma_long_now, 2) if pd.notnull(ma_long_now) else None,
                "Signal": signal
            })
        except Exception as e:
            # 예외 처리
            results.append({
                "Ticker": ticker,
                "Status": f"Error: {e}",
                "ShortMA": None,
                "LongMA": None,
                "Signal": None
            })
    
    return pd.DataFrame(results)
