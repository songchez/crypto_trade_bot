"""
__init__.py

detectors 패키지 초기화 및 공용 import 예시
"""

from .trend_change import detect_trend_change

__all__ = [
    "detect_trend_change",
]
