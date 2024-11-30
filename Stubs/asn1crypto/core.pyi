from __future__ import annotations

from typing import Dict, OrderedDict

from lfSignFont.authenticode import SpcIndirectDataContent

class AbstractString(Constructable, Primitive): ...
class Any(Asn1Value): ...

class Asn1Value(object):
    # def __init__(
    #     self,
    #     explicit: None | int | Tuple[Any, str] = None,
    #     implicit: None | int | Tuple[Any, str] = None,
    #     no_explicit: None | bool = False,
    #     tag_type: None | Literal["explicit"] | Literal["implicit"] = None,
    #     class_: None | Literal["application"] | Literal["context"] | Literal["private"] | Literal["universal"] = None,
    #     tag: None | int = None,
    #     optional=None,
    #     default=None,
    #     contents: None | bytes = None,
    #     method: None | int | Literal["constructed"] | Literal["primitive"] = None
    # ): ...

    @classmethod
    def load(cls, encoded_data: bytes, strict: bool = False, **kwargs): ...

class BMPString(AbstractString): ...
class Castable(object): ...

class Choice(Asn1Value):
    def __init__(
        self, name: None | str = None, value: None | str | Asn1Value = None, **kwargs
    ) -> None: ...

class Constructable(object): ...
class IA5String(AbstractString): ...
class Integer(Primitive, ValueMap): ...
class ObjectIdentifier(Primitive, ValueMap): ...
class OctetString(Constructable, Castable, Primitive): ...
class Primitive(Asn1Value): ...

class Sequence(Asn1Value):
    def __init__(
        self,
        value: None | Dict[str, str] | OrderedDict[str, object] = None,
        default: None | Dict[str, str] = None,
        **kwargs,
    ) -> None: ...
    def __getitem__(self, key: str): ...
    def __setitem__(self, key: str, value) -> None: ...
    def dump(self, force: bool = False) -> bytes: ...

class SequenceOf(Asn1Value): ...
class SetOf(SequenceOf): ...
class ValueMap: ...
