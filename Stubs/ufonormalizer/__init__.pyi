from __future__ import annotations

from pathlib import Path


DEFAULT_FLOAT_PRECISION = 10


def normalizeUFO(
    ufoPath: str,
    outputPath: str | None = None,
    onlyModified: bool = True,
    floatPrecision: int = DEFAULT_FLOAT_PRECISION,
    writeModTimes: bool = True,
): ...
