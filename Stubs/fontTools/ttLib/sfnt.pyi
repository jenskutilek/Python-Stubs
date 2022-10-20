from io import BufferedReader, BytesIO
from typing import BinaryIO, Optional, OrderedDict, Union


class SFNTReader(object):
    def __init__(
        self,
        file: BinaryIO,
        checkChecksums: int = 0,
        fontNumber: int = -1,
    ) -> None: ...

    def __getitem__(self, tag: str) -> bytes: ...

    @property
    def sfntVersion(self) -> str: ...

    @property
    def tables(self) -> OrderedDict: ...

    @tables.setter
    def tables(self, value: OrderedDict) -> None: ...

    def close(self) -> None: ...


class SFNTWriter(object):
    def __init__(self, file: BinaryIO, numTables: int, sfntVersion="\000\001\000\000",
			flavor: str | None = None, flavorData=None) -> None: ...
    
    def __setitem__(self, tag: str, data: bytes): ...
    
    def close(self) -> None: ...


class WOFFFlavorData():
    def __init__(self, reader: SFNTReader | None = None) -> None: ...
