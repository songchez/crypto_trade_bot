"""
ma_crossover.py

단기/장기 이동평균선 교차로 추세를 추종하는 전략
"""
import backtrader as bt

class MovingAverageCrossover(bt.Strategy):
    """
    - 단기/장기 MA 교차(골든크로스 -> 매수, 데드크로스 -> 매도)
    - 간단하지만 대표적인 추세 추종 방식
    """
    params = (
        ('fast_period', 20),
        ('slow_period', 60),
    )
    
    def __init__(self):
        self.ma_fast = bt.ind.SMA(self.data.close, period=self.p.fast_period)
        self.ma_slow = bt.ind.SMA(self.data.close, period=self.p.slow_period)
    
    def next(self):
        # 포지션이 없을 때
        if not self.position:
            # 골든크로스: (오늘) fast > slow 이고, (어제) fast <= slow
            if (self.ma_fast[0] > self.ma_slow[0]) and (self.ma_fast[-1] <= self.ma_slow[-1]):
                self.buy()
            # 데드크로스: (오늘) fast < slow 이고, (어제) fast >= slow
            elif (self.ma_fast[0] < self.ma_slow[0]) and (self.ma_fast[-1] >= self.ma_slow[-1]):
                self.sell()
        else:
            # 롱 포지션 -> fast가 slow 아래로 내려가면 청산
            if self.position.size > 0:
                if self.ma_fast[0] < self.ma_slow[0]:
                    self.close()
            # 숏 포지션 -> fast가 slow 위로 올라가면 청산
            elif self.position.size < 0:
                if self.ma_fast[0] > self.ma_slow[0]:
                    self.close()
