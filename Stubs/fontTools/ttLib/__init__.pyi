from __future__ import annotations

from io import BytesIO
from typing import Any, List, Optional, TypedDict, Union

from fontTools.ttLib.tables._g_l_y_f import table__g_l_y_f
from fontTools.ttLib.tables.DefaultTable import DefaultTable

class KnownTable(TypedDict):
    glyf: table__g_l_y_f

class TTFont(object):
    def __init__(
        self,
        file: Optional[Union[str, BytesIO]] = None,
        res_name_or_index: Optional[Union[str, int]] = None,
        sfntVersion: str = "\000\001\000\000",
        flavor: Optional[str] = None,
        checkChecksums: int = 0,
        verbose=None,
        recalcBBoxes: bool = True,
        allowVID=NotImplemented,
        ignoreDecompileErrors: bool = False,
        recalcTimestamp: bool = True,
        fontNumber: int = -1,
        lazy: Optional[bool] = None,
        quiet=None,
        _tableCache=None,
        cfg: dict = {},
    ) -> None: ...
    def __contains__(self, tag: str) -> bool: ...
    def __delitem__(self, tag: str) -> None: ...
    def __getitem__(self, tag: str) -> Any: ...
    def __setitem__(self, tag: str, table: Any) -> None: ...
    @property
    def flavor(self) -> str: ...
    @flavor.setter
    def flavor(self, value: str) -> None: ...
    def getBestCmap(
        self,
        cmapPreferences=(
            (3, 10),
            (0, 6),
            (0, 4),
            (3, 1),
            (0, 3),
            (0, 2),
            (0, 1),
            (0, 0),
        ),
    ): ...
    def getTableData(self, tag: str) -> bytes: ...
    def importXML(
        self, fileOrPath: Union[str, BytesIO], quiet: Optional[bool] = None
    ): ...
    def keys(self) -> List[str]: ...
    def save(self, file: Union[str, BytesIO], reorderTables: bool = True) -> None: ...
    def saveXML(
        self, fileOrPath: Union[str, BytesIO], newlinestr: str = "\n", **kwargs
    ): ...

def newTable(tag): ...
