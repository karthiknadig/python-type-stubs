from typing import Any

from ..en import Provider as AddressProvider

class Provider(AddressProvider):
    city_prefixes: Any = ...
    city_suffixes: Any = ...
    building_number_formats: Any = ...
    street_suffixes: Any = ...
    te_reo_parts: Any = ...
    te_reo_endings: Any = ...
    postcode_formats: Any = ...
    city_formats: Any = ...
    street_name_formats: Any = ...
    street_address_formats: Any = ...
    address_formats: Any = ...
    secondary_address_formats: Any = ...
    def state(self): ...
    def te_reo_part(self): ...
    def te_reo_first(self): ...
    def te_reo_ending(self): ...
    def city_prefix(self): ...
    def city_suffix(self): ...
    def rd_number(self): ...
    def secondary_address(self): ...
