from typing import Any

from .. import Provider as AutomotiveProvider

class Provider(AutomotiveProvider):
    license_plate_letters: Any = ...
    vehicle_categories: Any = ...
    license_plate_suffix: Any = ...
    license_plate_formats: Any = ...
    plate_number_formats: Any = ...
    plate_extra_formats: Any = ...
    plate_special_formats: Any = ...
    def license_plate(self): ...
    def plate_letter(self): ...
    def plate_number(self): ...
    def plate_number_extra(self): ...
    def plate_number_special(self): ...
    def plate_suffix(self): ...
    def vehicle_category(self): ...