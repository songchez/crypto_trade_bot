# """
# tradingview_webhook_example.py

# TradingView에서 보낸 Webhook을 수신하여
# 거래소 API에 주문을 내는 예시 코드 (Flask 기반)

# 주의: 학습용 예시이며, 실제 배포/보안 설정 필요
# """

# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     try:
#         data = request.json
#         # 예: {"ticker": "BTCUSDT", "price": 30000, "signal": "BUY"}
#         ticker = data.get('ticker')
#         signal = data.get('signal')
#         price = data.get('price')

#         # TODO: 거래소 API (예: binance, upbit)로 주문
#         # binance_client.order_market_buy(symbol=ticker, quantity=...)
#         # 또는 원하는 로직...

#         return jsonify({"status": "ok", "received": data}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# if __name__ == '__main__':
#     # 로컬에서 테스트 시
#     app.run(debug=True, port=5000)
