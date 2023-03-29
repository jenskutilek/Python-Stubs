from __future__ import annotations

from fontTools.pens.pointPen import AbstractPointPen
from typing import Any, Dict


class HashPointPen(AbstractPointPen):
    def __init__(
        self,
        glyphWidth: int = 0,
        glyphSet: Dict[str, Any] = None,
    ): ...
    def drawPoints(self) -> None: ...
    @property
    def hash(self) -> str: ...
