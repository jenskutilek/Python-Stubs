from __future__ import annotations

class Program:
    def fromAssembly(self, assembly: list[str] | str) -> None: ...
    def fromBytecode(self, bytecode: bytes) -> None: ...
    def getAssembly(self, preserve: bool = True) -> str: ...
    def getBytecode(self) -> bytes: ...
