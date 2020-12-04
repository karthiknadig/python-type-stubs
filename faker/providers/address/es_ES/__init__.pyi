from typing import Any

from ..es import Provider as AddressProvider

class Provider(AddressProvider):
    building_number_formats: Any = ...
    street_prefixes: Any = ...
    postcode_formats: Any = ...
    states: Any = ...
    city_formats: Any = ...
    street_name_formats: Any = ...
    street_address_formats: Any = ...
    address_formats: Any = ...
    secondary_address_formats: Any = ...
    def state_name(self): ...
    def street_prefix(self): ...
    def secondary_address(self): ...
    def state(self): ...
