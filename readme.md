# 백테스트봇S

백테스트봇S는 사용자가 선택한 전략을 기반으로 주식 및 암호화폐의 백테스트를 수행할 수 있는 Streamlit 기반의 웹 애플리케이션입니다. 이 애플리케이션은 다양한 전략을 지원하며, 사용자 친화적인 UI를 통해 데이터를 다운로드하고 분석 결과를 시각화합니다.

## 기능

- **데이터 다운로드**: 사용자가 입력한 티커에 대한 OHLCV(시가, 고가, 저가, 종가, 거래량) 데이터를 Yahoo Finance에서 다운로드합니다.
- **전략 실행**: 다양한 거래 전략을 선택하고, 해당 전략에 따라 백테스트를 수행합니다.
- **결과 시각화**: 백테스트 결과를 시각적으로 표현하여 사용자가 쉽게 이해할 수 있도록 합니다.

## 설치

1. **필수 라이브러리 설치**: `requirements.txt` 파일을 사용하여 필요한 라이브러리를 설치합니다.

```bash
pip install -r requirements.txt
```

2. **Streamlit 실행**: 아래 명령어로 애플리케이션을 실행합니다.

```bash
streamlit run main.py
```

## 파일 구조

```bash
 ├── main.py # 애플리케이션의 진입점
 ├── components # UI 및 전략 실행 관련 모듈
 │ ├── data_fetcher.py # 데이터 다운로드 기능
 │ ├── strategies.py # 전략 실행 기능
 │ └── ui.py # 사용자 인터페이스 렌더링
 ├── strategies # 다양한 거래 전략 구현
 │ ├── bollinger_band.py # 볼린저 밴드 전략
 │ ├── rsi_macd_sto.py # RSI, MACD, Stochastic 전략
 │ ├── supertrend.py # 슈퍼트렌드 전략
 │ └── trailing_stop.py # 트레일링 스톱 전략
 └── requirements.txt # 필요한 라이브러리 목록
```

## 사용법

1. **티커 입력**: 분석할 주식 또는 암호화폐의 티커를 입력합니다. 여러 개의 티커를 입력할 수 있습니다.
2. **날짜 선택**: 데이터 다운로드를 위한 시작 날짜와 종료 날짜를 선택합니다.
3. **전략 선택**: 사용할 거래 전략을 선택합니다.
4. **전략 파라미터 설정**: 선택한 전략에 따라 필요한 파라미터를 설정합니다.
5. **데이터 다운로드 및 전략 실행**: 버튼을 클릭하여 데이터를 다운로드하고 선택한 전략을 실행합니다.

## 기여

기여를 원하시는 분은 이 저장소를 포크한 후, 변경 사항을 커밋하고 풀 리퀘스트를 제출해 주세요.

## 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다.
