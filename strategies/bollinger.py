"""
bollinger.py

볼린저 밴드 상/하단 돌파를 이용한 추세 추종 전략
"""
import backtrader as bt

class BollingerBreakoutStrategy(bt.Strategy):
    """
    - 볼린저 상단 돌파 시 상승 추세로 보고 매수,
      하단 돌파 시 하락 추세로 보고 매도
    - 추세가 꺾이면(중심선 기준) 청산
    """
    params = (
        ('period', 20),
        ('devfactor', 2.0),
    )
    
    def __init__(self):
        self.bb = bt.ind.BollingerBands(
            self.data.close,
            period=self.p.period,
            devfactor=self.p.devfactor
        )
        # self.bb.top, self.bb.mid, self.bb.bot
    
    def next(self):
        if not self.position:
            # 상단선 돌파 -> 매수
            if self.data.close[0] > self.bb.top[0]:
                self.buy()
            # 하단선 돌파 -> 매도
            elif self.data.close[0] < self.bb.bot[0]:
                self.sell()
        else:
            # 롱 상태 -> 중심선 밑으로 내려가면 청산
            if self.position.size > 0 and self.data.close[0] < self.bb.mid[0]:
                self.close()
            # 숏 상태 -> 중심선 위로 올라가면 청산
            elif self.position.size < 0 and self.data.close[0] > self.bb.mid[0]:
                self.close()
