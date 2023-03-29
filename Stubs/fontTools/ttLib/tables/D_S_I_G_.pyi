from __future__ import annotations

from typing import List, Literal, OrderedDict
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables import DefaultTable


class table_D_S_I_G_(DefaultTable.DefaultTable):
    def __init__(self, tag: Literal["DSIG"]) -> None: ...

    @property
    def ulVersion(self) -> int: ...

    @ulVersion.setter
    def ulVersion(self, value: int) -> None: ...

    @property
    def usNumSigs(self) -> int: ...

    @usNumSigs.setter
    def usNumSigs(self, value: int) -> None: ...

    @property
    def usFlag(self) -> int: ...

    @usFlag.setter
    def usFlag(self, value: int) -> None: ...

    @property
    def signatureRecords(self) -> List: ...

    @signatureRecords.setter
    def signatureRecords(self, value: OrderedDict) -> None: ...

    def compile(self, ttFont: TTFont | None) -> bytes: ...

class SignatureRecord(object): ...

pem_spam = lambda l, spam = {
	"-----BEGIN PKCS7-----": True, "-----END PKCS7-----": True, "": True
}: not spam.get(l.strip())
