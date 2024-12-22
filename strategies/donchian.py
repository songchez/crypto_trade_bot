"""
donchian.py

Donchian Channel 기반 추세추종 전략
(일명 '터틀 트레이딩'의 핵심 개념)
"""
import backtrader as bt

class DonchianBreakoutStrategy(bt.Strategy):
    """
    - Donchian 채널을 이용해 최근 N일 최고가/최저가 돌파로
      매수/매도 신호를 생성
    - 역돌파가 나오면 포지션 청산
    """
    params = (
        ('donchian_period', 20),  # 채널 기간
    )
    
    def __init__(self):
        # 최고가/최저가 지표
        self.highest = bt.ind.Highest(self.data.high, period=self.p.donchian_period)
        self.lowest = bt.ind.Lowest(self.data.low, period=self.p.donchian_period)
        
    def next(self):
        # 포지션(롱/숏) 보유 중인지 확인
        if not self.position:
            # 롱 진입 신호: 이전 봉의 최고가 돌파
            if self.data.close[0] > self.highest[-1]:
                self.buy()
            # 숏 진입 신호: 이전 봉의 최저가 하락 돌파
            elif self.data.close[0] < self.lowest[-1]:
                self.sell()
        else:
            # 롱 포지션 청산 조건
            if self.position.size > 0 and self.data.close[0] < self.lowest[-1]:
                self.close()
            # 숏 포지션 청산 조건
            elif self.position.size < 0 and self.data.close[0] > self.highest[-1]:
                self.close()
