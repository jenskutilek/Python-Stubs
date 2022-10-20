from datetime import datetime
from asn1crypto.core import Sequence

class Certificate(Sequence):
    @property
    def issuer(self) -> str: ...

    @property
    def not_valid_after(self) -> datetime: ...

    @property
    def not_valid_before(self) -> datetime: ...

    @property
    def serial_number(self) -> int: ...
