import streamlit as st

# 프로젝트 소개
st.title("🐢 터틀 백테스트봇S - 사용 설명서")

st.markdown("""
**안녕하세요!**
**Crypto Trade Bot**에 오신 것을 환영합니다.
이 프로젝트는 **Streamlit**과 **Python**으로 작성된 고급 트레이딩 봇으로, 다양한 **기술적 지표**와 **트렌드 기반 전략**을 사용해 데이터를 분석하고 백테스트를 수행할 수 있습니다.

---

## 🌟 주요 기능
- **SuperTrend, 볼린저밴드, 트레일링스탑, RSI&MACD&Stochastic 등 다양한 전략**
- 유연한 **기준봉 설정** (5분, 15분, 1시간, 4시간 등)
- 실시간 데이터 분석 및 **백테스팅 결과 시각화**
- 직관적인 **수익률 계산** 및 **전략 비교**

---

## 🛠️ 사용법
### 1️⃣ 각 파라미터 설명
🐢 터틀 백테스트봇S은 다양한 파라미터로 다양하게 백테스팅 해볼 수 있습니다.
1. **티커입력**: 본 웹앱은 [야후파이낸스API](https://finance.yahoo.com/)를 통해서 제작되었으므로
            야후파이낸스에서 쓰이는 티커와 데이터를 기준으로 백테스팅 하였습니다.
            ⚠️주의할점은, 띄어쓰기를 포함하지 않고 쉼표로만 구분해주셔야 합니다!
            그리고 너무 많은 티커를 넣을경우도 오류발생의 원인이 되니 주의해주세요.
2. **자본금**: 백테스팅의 첫 시작 자본금입니다
3. **시작날짜**, 종료날짜, 기준봉: 기준봉에 따라 가능한 시작날짜, 종료날짜가 다르니 확인 후 백테스팅 해주세요!
4. **수수료율**: 각 거래마다 소요되는 수수료입니다.
5. **전략선택**: 가장 중요한 전략! 기준봉을 바꿔가며 같은전략이더라도 투자패턴의 변화를 줘보세요! 수익률이 크게 달라지거든요!
6. **커스텀 파라미터**: ex)ATR기간, Multiplier


### 2️⃣ 실행 방법
```bash
streamlit run main.py
```
명령어를 실행하면 **웹 브라우저**에서 트레이딩 봇 인터페이스가 열립니다.  
티커, 기간, 기준봉(interval), 전략을 선택하고 데이터를 분석하세요!

### 3️⃣ 백테스팅 시작
1. **티커**를 입력하세요 (예: BTC-USD, AAPL).
2. 기간과 기준봉을 설정합니다.
3. 원하는 전략과 파라미터를 선택합니다.
4. 결과 페이지에서 백테스팅 결과 및 수익률을 확인하세요!

---

## 📖 주요 전략
### **1. SuperTrend**
변동성과 추세를 기반으로 하는 **추세추종 전략**으로, 상승 및 하락 추세를 간단히 분석할 수 있습니다.

- **매수 신호**: 상승 추세 진입 시
- **매도 신호**: 하락 추세 진입 시

### **2. RSI & MACD & Stochastic**
이 전략은 RSI, MACD, Stochastic 지표를 결합하여 **과매수/과매도**를 기반으로 매매 신호를 생성합니다.

- **매수 신호**: RSI > 50, MACD > Signal, Stochastic < 20
- **매도 신호**: RSI < 50, MACD < Signal, Stochastic > 80

### **3. Bollinger Band**
**볼린저 밴드**는 가격의 평균과 표준편차를 사용하여 **지지선과 저항선**을 형성합니다.  
밴드 돌파를 이용한 전략을 통해 **추세 반전**을 확인합니다.

---

## 🧐 FAQ (자주 묻는 질문)

### 1️⃣ **전략을 실제 매매에 이용하려면 어떻게 해야 하나요?**
Crypto Trade Bot은 **백테스팅**을 위해 설계되었습니다.  
실제 매매에 활용하려면, **API**(예: Binance API)를 추가로 통합하여 주문 실행 로직을 구현해야 합니다.  
예시:
```python
from binance.client import Client
client = Client(api_key, api_secret)
```
추가 로직은 추후 구독회원에게만 공개될 예정입니다!

### 2️⃣ **새로운 전략을 테스트해보고 싶어요!**
1. 프로젝트 폴더의 `strategies` 디렉토리에서 새로운 전략 파일을 작성하세요.
2. **main.py**에서 새 전략을 선택할 수 있도록 UI를 추가하세요.
3. Streamlit UI를 업데이트하여 파라미터를 입력받고, 결과를 확인하세요.

### 3️⃣ **오류가 났을 땐 어떻게 해야 하나요?**
- **데이터 관련 오류**: Yahoo Finance API는 특정 조건에서 데이터를 제공하지 않을 수 있습니다.  
  날짜, 티커, 기준봉(interval)이 올바른지 확인하세요.
- **코드 관련 오류**: 에러 메시지를 확인하고, GitHub 이슈 페이지에 보고하세요.
- **FAQ로 해결되지 않는 경우**: [GitHub Discussions](https://github.com/songchez/crypto_trade_bot/discussions)에서 도움을 요청하세요.

### 4️⃣ **수익률이 예상과 다릅니다.**
수익률 계산에 영향을 줄 수 있는 **수수료** 및 **기타 비용**을 확인하세요.  
또한, 설정한 기간과 전략이 일치하는지 검토하세요.

---

## 🤝 기여하기
1. 새로운 기능 아이디어를 [해당 GitHub](https://github.com/songchez/crypto_trade_bot/issues)에 등록하세요.
2. 프로젝트를 **Fork**하고 개선 사항을 반영한 후 **Pull Request**를 만들어주세요.

---

## ☕️ 개발자에게 커피 한 잔 사주세요!

여러분이 한잔씩 사주시는 커피는 개발자에게 큰 힘이 된답니다. 👍👍

<a href="https://www.buymeacoffee.com/tama4840X" target="_blank">
    <img src="https://img.buymeacoffee.com/button-api/?text=Buy me a Coffee&emoji=&slug=tama4840X&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" />
</a>

---

## 🚀 앞으로 추가될 수(?)도 있는 기능
- [ ] Binance API를 통한 **실제 매매 실행**
- [ ] AI 알고리즈믹 **전략 최적화** 및 **자동 튜닝**
- [ ] **알림 시스템**: 텔레그램, 이메일, SMS 알림 및 각종 거래소 API 연동
- [ ] 더 많은 **기술적 지표 및 전략** 추가
- [ ] 포트폴리오 관리 기능
- [ ] 다양한 데이터 소스 통합 (Alpha Vantage, Quandl 등)

---

📢 질문이나 의견이 있다면 연락 주세요 
""", unsafe_allow_html=True)