from typing import Any, Optional, Tuple

class AbstractPointPen:
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
        **kwargs: Any
    ) -> None: ...
    def addComponent(
        self,
        glyphName: str,
        transformation: Tuple[float, float, float, float, float, float],
        identifier: Optional[str] = None,
        **kwargs: Any
    ) -> None: ...
