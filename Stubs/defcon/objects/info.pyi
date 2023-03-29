from __future__ import annotations

from defcon.objects.base import BaseObject

class Info(BaseObject):
    @property
    def openTypeGaspRangeRecords(self): ...
    @property
    def openTypeHeadFlags(self): ...
    @property
    def openTypeHeadLowestRecPPEM(self) -> int: ...
