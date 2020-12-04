from typing import Any

from .. import BaseProvider as BaseProvider

localized: bool

class Provider(BaseProvider):
    local_prefixes: Any = ...
    def ean(self, length: int = ..., prefixes: Any = ...): ...
    def ean8(self, prefixes: Any = ...): ...
    def ean13(self, prefixes: Any = ...): ...
    def localized_ean(self, length: int = ...): ...
    def localized_ean8(self): ...
    def localized_ean13(self): ...