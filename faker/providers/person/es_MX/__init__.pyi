from typing import Any

from .. import Provider as PersonProvider

class Provider(PersonProvider):
    formats: Any = ...
    first_names: Any = ...
    last_names: Any = ...
    prefixes: Any = ...
