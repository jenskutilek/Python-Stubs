from __future__ import annotations


class DefaultTable(object):
    def __init__(self, tag: str | None = None) -> None: ...

    @property
    def data(self) -> bytes: ...

    @data.setter
    def data(self, value: bytes) -> None: ...
