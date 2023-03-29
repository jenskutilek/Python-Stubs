from __future__ import annotations

from defcon.objects.font import Font
from fontTools.pens.pointPen import AbstractPointPen
from typing import Any, Dict


class HashPointPen(AbstractPointPen):
    def __init__(
        self,
        glyphWidth: int = 0,
        glyphSet: Dict[str, Any] | Font | None = None,
    ): ...
    def drawPoints(self) -> None: ...
    @property
    def hash(self) -> str: ...
