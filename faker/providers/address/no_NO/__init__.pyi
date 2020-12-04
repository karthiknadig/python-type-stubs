from typing import Any

from .. import Provider as AddressProvider

class Provider(AddressProvider):
    city_suffixes: Any = ...
    street_suffixes: Any = ...
    city_formats: Any = ...
    street_name_formats: Any = ...
    street_address_formats: Any = ...
    address_formats: Any = ...
    building_number_formats: Any = ...
    building_number_suffixes: Any = ...
    postcode_formats: Any = ...
    def building_number(self): ...
    def city_suffix(self): ...
    def street_suffix(self): ...