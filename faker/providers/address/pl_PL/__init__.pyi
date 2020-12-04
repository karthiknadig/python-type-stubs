from typing import Any

from .. import Provider as AddressProvider

class Provider(AddressProvider):
    cities: Any = ...
    street_prefixes: Any = ...
    streets: Any = ...
    regions: Any = ...
    building_number_formats: Any = ...
    postcode_formats: Any = ...
    street_address_formats: Any = ...
    address_formats: Any = ...
    def street_prefix(self): ...
    def street_prefix_short(self): ...
    def street_name(self): ...
    def city(self): ...
    def region(self): ...
