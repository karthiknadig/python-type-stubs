from typing import Any

from .. import Provider as BarcodeProvider

class Provider(BarcodeProvider):
    local_prefixes: Any = ...
    def jan(self, length: int = ...): ...
    def jan8(self): ...
    def jan13(self): ...