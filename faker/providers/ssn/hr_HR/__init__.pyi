from typing import Any

from .. import Provider as SsnProvider

def checksum(digits: Any): ...

class Provider(SsnProvider):
    def ssn(self): ...
    vat_id_formats: Any = ...
    def vat_id(self): ...
