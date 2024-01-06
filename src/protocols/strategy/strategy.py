import typing as tp
from src.protocols.predict.prediction import PredictionProtocol
from src.protocols.position.open_position import OpenPositionProtocol
from src.protocols.position.close_position import ClosePositionProtocol
from src.protocols.risk.risk import RiskProtocol
from src.protocols.limits.limit import LimitProtocol


class StrategyProtocol(tp.Protocol):
    """Protocol of strategy"""

    async def limits(self) -> LimitProtocol:
        """"""

    async def predict(self) -> PredictionProtocol:
        """"""

    async def open_position(self) -> OpenPositionProtocol:
        """"""

    async def close_position(self) -> ClosePositionProtocol:
        """"""

    async def risk(self) -> RiskProtocol:
        """"""
