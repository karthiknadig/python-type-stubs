from typing import Any

from .. import BaseProvider as BaseProvider

localized: bool

class Provider(BaseProvider):
    country_calling_codes: Any = ...
    formats: Any = ...
    msisdn_formats: Any = ...
    def phone_number(self): ...
    def country_calling_code(self): ...
    def msisdn(self): ...