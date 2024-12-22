"""
__init__.py

패키지 초기화 및 공용 import 예시:
- donchian, ma_crossover, bollinger 모듈에서 필요한 클래스를
  한 번에 임포트하여 사용자가 간편하게 가져다 쓸 수 있게끔 설정.
"""

from .donchian import DonchianBreakoutStrategy
from .ma_crossover import MovingAverageCrossover
from .bollinger import BollingerBreakoutStrategy

# __all__은 이 패키지에서 공개할 모듈/클래스의 목록을 지정할 때 사용
__all__ = [
    "DonchianBreakoutStrategy",
    "MovingAverageCrossover",
    "BollingerBreakoutStrategy",
]
