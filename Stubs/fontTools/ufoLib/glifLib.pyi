from __future__ import annotations

from fontTools.pens.pointPen import AbstractPointPen
from fontTools.ufoLib import _UFOBaseIO
from pathlib import Path
from typing import Any, Optional, Tuple, Callable

class GLIFPointPen(AbstractPointPen):
    def __init__(
        self, element, formatVersion=None, identifiers=None, validate=True
    ): ...
    def beginPath(
        self, identifier: Optional[str] = None, **kwargs: Any
    ) -> None: ...
    def endPath(self) -> None: ...
    def addPoint(
        self,
        pt: Tuple[float, float],
        segmentType: Optional[str] = None,
        smooth: bool = False,
        name: Optional[str] = None,
        identifier: Optional[str] = None,
        **kwargs: Any,
    ) -> None: ...
    def addComponent(
        self,
        glyphName: str,
        transformation: Tuple[float, float, float, float, float, float],
        identifier: Optional[str] = None,
        **kwargs: Any,
    ) -> None: ...

class Glyph:
    def __init__(self, glyphName, glyphSet) -> None: ...
    def draw(self, pen, outputImpliedClosingLine=False) -> None: ...
    def drawPoints(self, pointPen) -> None: ...

class GlyphSet(_UFOBaseIO):
    def __init__(
        self,
        path: Path,
        glyphNameToFileNameFunc: Callable | None = None,
        ufoFormatVersion: int | None = None,
        validateRead: bool = True,
        validateWrite: bool = True,
        expectContentsFile: bool = False,
    ) -> None: ...
    def writeContents(self) -> None: ...
    def writeGlyph(
        self,
        glyphName: str,
        glyphObject: Any = None,
        drawPointsFunc: Callable | None = None,
        formatVersion: int | None = None,
        validate=None,
    ) -> None: ...
    def writeLayerInfo(self, info, validateWrite=None) -> None: ...
