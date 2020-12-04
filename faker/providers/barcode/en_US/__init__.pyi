from typing import Any, Optional

from .. import Provider as BarcodeProvider

class Provider(BarcodeProvider):
    local_prefixes: Any = ...
    upc_e_base_pattern: Any = ...
    upc_ae_pattern1: Any = ...
    upc_ae_pattern2: Any = ...
    upc_ae_pattern3: Any = ...
    def ean13(self, leading_zero: Optional[Any] = ..., prefixes: Any = ...): ...
    def upc_a(
        self,
        upc_ae_mode: bool = ...,
        base: Optional[Any] = ...,
        number_system_digit: Optional[Any] = ...,
    ): ...
    def upc_e(
        self,
        base: Optional[Any] = ...,
        number_system_digit: Optional[Any] = ...,
        safe_mode: bool = ...,
    ): ...
