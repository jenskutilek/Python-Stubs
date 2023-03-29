from __future__ import annotations

from defcon.objects.base import BaseObject
from defcon.objects.info import Info
from typing import List


class Font(BaseObject):
    def __init__(
        self,
        path: str | None = None,
        kerningClass=None,
        infoClass=None,
        groupsClass=None,
        featuresClass=None,
        libClass=None,
        unicodeDataClass=None,
        layerSetClass=None,
        layerClass=None,
        imageSetClass=None,
        dataSetClass=None,
        guidelineClass=None,
        glyphClass=None,
        glyphContourClass=None,
        glyphPointClass=None,
        glyphComponentClass=None,
        glyphAnchorClass=None,
        glyphImageClass=None,
    ):
        ...

    def _get_guidelines(self):
        ...

    def _set_guidelines(self, value: List):
        ...

    guidelines = property(
        _get_guidelines,
        _set_guidelines,
        doc="An ordered list of :class:`Guideline` objects stored in the font. Setting this will post a *Font.Changed* notification along with any notifications posted by the :py:meth:`Font.appendGuideline` and :py:meth:`Font.clearGuidelines` methods.",
    )

    def _get_lib(self):
        ...

    lib = property(_get_lib, doc="The font's :class:`Lib` object.")

    def _set_path(self, path: str) -> None:
        ...

    def _get_path(self) -> str | None:
        ...

    path = property(_get_path, _set_path, doc="The location of the file on disk. Setting the path should only be done when the user has moved the file in the OS interface. Setting the path is not the same as a save operation.")

    def __iter__(self):
        ...

    def _get_info(self) -> Info:
        ...

    info = property(_get_info, doc="The font's :class:`Info` object.")

    def keys(self): ...

    def save(
        self,
        path: str | None = None,
        formatVersion=None,
        removeUnreferencedImages=False,
        progressBar=None,
        structure=None,
    ):
        ...
