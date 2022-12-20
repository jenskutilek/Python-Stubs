from __future__ import annotations

from defcon.objects.base import BaseObject
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

    def __iter__(self):
        ...

    def save(
        self,
        path: str | None = None,
        formatVersion=None,
        removeUnreferencedImages=False,
        progressBar=None,
        structure=None,
    ):
        ...
