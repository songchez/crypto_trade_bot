# README

## 프로젝트 개요

본 프로젝트는 **추세 추종(Trend Following) 전략**을 자동으로 백테스팅하고, 시각화하며, 다양한 자산군(티커)의 **추세 전환**을 감지하는 **Streamlit** 웹 애플리케이션 예시입니다.

- **주요 특징**
  1. **Backtrader** 라이브러리를 사용한 백테스팅 (여러 가지 추세 추종 전략 제공)
  2. **Streamlit**을 통한 웹 UI 및 시각화 (차트, 성과 지표)
  3. **여러 티커의 추세 전환(골든/데드 크로스) 자동 감지** 기능
  4. **TradingView Webhook** (옵션) 연동 개념 예시

> **주의**: 학습 및 데모용이며, 실제 투자에서는 수수료·슬리피지·오버피팅 등 여러 위험 요소에 주의해야 합니다.

---

## 폴더 구조

````bash
my_trend_following_app/


버전:
python3.12.8


1. **`strategies/`**

   - **Backtrader**용 전략 클래스를 모아둔 폴더.
   - `donchian.py` (Donchian Breakout), `ma_crossover.py` (이동평균 교차), `bollinger.py` (볼린저 밴드 돌파).
   - `__init__.py`에서 필요한 클래스를 재정의/공개하여 쉽게 import 가능.

2. **`detectors/`**

   - 여러 자산의 추세 전환 감지 기능을 구현.
   - 현재는 `trend_change.py`에서 **단기/장기 이동평균 교차**를 통해 “골든/데드크로스” 발생을 체크.

3. **`main_app.py`**

   - **Streamlit** 메인 애플리케이션 파일.

   1. 개별 티커 백테스트 (사용자 입력 → 데이터 다운로드 → 전략 적용 → 결과 차트 표시)
   2. 다중 티커 추세 전환 감지 (테이블 표시)

4. **`tradingview_webhook_example.py`** (옵션)

   - **Flask**를 사용한 간단한 웹서버 예시로, TradingView Webhook 수신 → 거래소 API 호출 로직 샘플.
   - 실제 운영 시에는 인증, 보안, 주문체결 로직 등을 추가 구현해야 함.

5. **`requirements.txt`**

   - 프로젝트 실행에 필요한 라이브러리 목록 (Streamlit, Backtrader, yfinance, matplotlib 등).

6. **`README.md`**
   - 현재 문서(프로젝트 개요, 실행 방법 등).

---

## 실행 방법

### 1) 환경 설치

1. (선택) **가상환경** 생성

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # (Windows: venv\Scripts\activate)
````

2. 필수패키지 설치

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### 2) 백테스트 앱 실행

```bash
streamlit run main_app.py
```

- 터미널에 표시된 로컬 URL(예: <http://localhost:8501)로> 브라우저 접속
- 사이드바 또는 화면에서:

1. 티커(symbol) 입력
2. 기간 설정(시작/종료 날짜)
3. 전략 선택 / 파라미터 입력 (Donchian, MA Crossover, Bollinger 등)
4. 실행 버튼 클릭 → 백테스트 결과 차트 및 수익률 표시

- 아래 섹션에서 다중 티커 추세 전환 감지도 실행 가능

### 3) TradingView Webhook (옵션)

- tradingview_webhook_example.py는 단순 Flask 웹 서버 예시로,

1. python tradingview_webhook_example.py 실행 → http://<서버IP>:5000/webhook
2. TradingView Alert → Webhook URL 설정
3. Webhook 받으면, JSON 메시지 파싱 후 거래소 API(바이낸스/업비트 등)로 주문 시도

---

## 전략 소개

1. Donchian Breakout (터틀 트레이딩류)

최근 N일(봉) 중 최고가/최저가 돌파에 따라 매매.
횡보장에서 가짜 돌파가 잦을 수 있으나, 큰 추세가 발생하면 수익 극대화 가능. 2. Moving Average Crossover

단기 MA(예: 20일) vs. 장기 MA(예: 60일) 교차점으로 매수/매도 신호.
추세가 명확히 형성되면 수익을 낼 수 있지만, 횡보장에서 잦은 교차(손절)가 생길 수 있음. 3. Bollinger Breakout

볼린저 밴드 상단 돌파 시 상승 추세 진입(매수), 하단 돌파 시 하락 추세 진입(매도).
추세가 꺾일 때 중심선(mid) 기준으로 청산.

---

## 주의사항

1. **투자 리스크**

   - 본 코드는 학습/연구용이며, 실제 투자 손익은 책임지지 않습니다.
   - 암호화폐, 주식, 선물 등 시장은 변동성이 크고 예측 불가능한 요소가 많습니다.

2. **오버피팅**

   - 백테스팅에서 과거 데이터에만 지나치게 최적화된 전략은 실전에서 성과를 못 낼 위험이 있습니다.
   - 워크포워드 테스트(Out-of-sample), 샘플 분리 등을 통해 검증이 필요합니다.

3. **슬리피지, 스프레드, 수수료**

   - 실제 체결가는 시뮬레이션과 다를 수 있으므로, **수수료 및 슬리피지**를 현실적으로 반영해야 합니다.

4. **서버 보안 및 안정성**
   - TradingView Webhook 적용 시, 인증 토큰 설정/HTTPS 적용 등 보안이 필수입니다.
   - 서버 장애, 네트워크 지연, 거래소 API 에러 등에 대한 예외 처리도 중요합니다.

## 확장 아이디어

### 1. 포지션 사이징, 리스크 관리

- **ATR(평균 변동성) 기반 포지션 크기 조절**
  - 변동성이 큰 종목에 대한 포지션 축소, 변동성이 작은 종목에 대한 포지션 확대 등
- **손절선(Stop-Loss) 자동 적용**
  - 일정 변동성(ATR) 범위 혹은 고정 퍼센트 단위로 손절 라인을 설정해 리스크 제한
- **최대 손실 제한**
  - 하루/월별 손실 한도를 정하고 넘어가면 모든 포지션을 강제 청산
- **포트폴리오 분산**
  - 여러 종목(또는 코인, 주식, 선물 등)을 동시에 매매하여 리스크 분산

### 2. 멀티 타임프레임 분석

- **일봉 + 주봉/4시간봉 등 상위 차트**
  - 상위 차트의 추세가 일치할 때만 진입하는 필터를 적용해, 신호의 정확도 향상

### 3. 추가 지표/전략

- **Ichimoku, SuperTrend, MACD, RSI 등**
  - 추세/모멘텀 지표를 다각도로 결합하여 전략 성능 강화
- **머신러닝/딥러닝**
  - 패턴 인식, 시계열 예측 모델로 추세 전환 포착 등 고급 기법 연구

### 4. 데이터 소스 다변화

- **yfinance** 외에 **CCXT(암호화폐 거래소)**, **Interactive Brokers**(해외선물/주식), **Quandl** 등
  - 더 다양한 시장과 실시간 데이터에 대응하기 위한 API/라이브러리 활용

### 5. 실시간 자동매매

- **프로젝트를 서버에 배포**, **거래소 API**로 주문
  - 주문 체결 이후 사고 대응(서버 재부팅, 예외처리), UI 알람(Slack, Discord 등), 손익 보고 자동화
- **트레이딩뷰 Webhook**, **플랫폼 연동**
  - 트레이딩뷰에서 발생한 신호를 서버로 받아 곧바로 주문 실행

---

## 라이선스 (예시)

본 예시는 **MIT License** 아래 무료로 공개된 예시 코드이며,  
어떠한 보증도 없으며, 사용에 따른 책임은 전적으로 사용자에게 있습니다.

```scss
MIT License

Copyright (c) 2023

Permission is hereby granted, free of charge, ...
[이하 생략]

```
