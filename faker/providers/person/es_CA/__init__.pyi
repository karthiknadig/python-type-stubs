from typing import Any

from ..es_ES import Provider as PersonProvider

class Provider(PersonProvider):
    first_names_male: Any = ...
    first_names_female: Any = ...
    first_names: Any = ...