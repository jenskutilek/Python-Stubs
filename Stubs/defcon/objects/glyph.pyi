from __future__ import annotations

from defcon.objects.base import BaseObject
from typing import List, Tuple


class Glyph(BaseObject):
    def _get_components(self) -> List:
        ...

    components = property(
        _get_components,
        doc="An ordered list of :class:`Component` objects stored in the glyph.",
    )

    def __len__(self) -> int:
        ...

    def _get_bounds(self) -> Tuple[float, float, float, float]:
        ...

    bounds = property(_get_bounds, doc="The bounds of the glyph's outline expressed as a tuple of form (xMin, yMin, xMax, yMax).")

    def _set_name(self, value: str) -> None:
        ...

    def _get_name(self) -> str:
        ...

    name = property(
        _get_name,
        _set_name,
        doc="The name of the glyph. Setting this posts *GLyph.NameChanged* and *Glyph.NameChanged* notifications.",
    )

    def _get_width(self) -> float:
        ...

    def _set_width(self, value) -> None:
        ...

    width = property(_get_width, _set_width, doc="The width of the glyph. Setting this posts *Glyph.WidthChanged* and *Glyph.Changed* notifications.")
