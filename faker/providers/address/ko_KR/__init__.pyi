from typing import Any

from .. import Provider as AddressProvider

ALPHABET: Any

class Provider(AddressProvider):
    building_suffixes: Any = ...
    road_suffixes: Any = ...
    town_suffixes: Any = ...
    postcode_formats: Any = ...
    new_postal_code_formats: Any = ...
    metropolitan_cities: Any = ...
    provinces: Any = ...
    cities: Any = ...
    road_names: Any = ...
    boroughs: Any = ...
    countries: Any = ...
    building_dongs: Any = ...
    land_numbers: Any = ...
    road_numbers: Any = ...
    town_formats: Any = ...
    building_name_formats: Any = ...
    address_detail_formats: Any = ...
    road_formats: Any = ...
    road_address_formats: Any = ...
    land_address_formats: Any = ...
    city_suffixes: Any = ...
    street_suffixes: Any = ...
    street_name_formats: Any = ...
    street_address_formats: Any = ...
    address_formats: Any = ...
    def land_number(self): ...
    def land_address(self): ...
    def road_number(self): ...
    def road_address(self): ...
    def address_detail(self): ...
    def road(self): ...
    def road_name(self): ...
    def road_suffix(self): ...
    def metropolitan_city(self): ...
    def province(self): ...
    def city(self): ...
    def borough(self): ...
    def town(self): ...
    def town_suffix(self): ...
    def building_name(self): ...
    def building_suffix(self): ...
    def building_dong(self): ...
    def old_postal_code(self): ...
    def postcode(self): ...
    def postal_code(self): ...