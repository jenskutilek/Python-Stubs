from __future__ import annotations

import enum
from pathlib import Path
from typing import Any, Dict, List, Tuple

class _UFOBaseIO: ...
class UFOReader(_UFOBaseIO): ...

class UFOWriter(UFOReader):
    def __init__(
        self,
        path: Path,
        formatVersion: Tuple[int, int] | int | None = None,
        fileCreator: str = "com.github.fonttools.ufoLib",
        structure=None,
        validate: bool = True,
    ) -> None: ...
    def getGlyphSet(
        self,
        layerName=None,
        defaultLayer=True,
        glyphNameToFileNameFunc=None,
        validateRead=None,
        validateWrite=None,
        expectContentsFile=False,
    ): ...
    def writeFeatures(self, features: str, validate=None) -> None: ...
    def writeGroups(self, groups: Dict[str, List[str]], validate=None) -> None: ...
    def writeInfo(self, info: Any, validate=None) -> None: ...
    def writeKerning(self, kerning: Dict, validate=None) -> None: ...
    def writeLayerContents(self, layerOrder=None, validate=None) -> None: ...
    def writeLib(self, libDict: Dict[str, Any], validate=None) -> None: ...
    def close(self) -> None: ...

class UFOFileStructure(enum.Enum):
    ZIP = "zip"
    PACKAGE = "package"
