from __future__ import annotations


class Program:
    def fromBytecode(self, bytecode: bytes) -> None:
        ...

    def getAssembly(self, preserve: bool = True) -> str:
        ...
