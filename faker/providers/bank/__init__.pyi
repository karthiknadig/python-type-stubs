from typing import Any

from .. import BaseProvider as BaseProvider

localized: bool
default_locale: str

class Provider(BaseProvider):
    ALPHA: Any = ...
    bban_format: str = ...
    country_code: str = ...
    def bank_country(self): ...
    def bban(self): ...
    def iban(self): ...
