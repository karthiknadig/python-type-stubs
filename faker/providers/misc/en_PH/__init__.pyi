from typing import Any

from .. import Provider as MiscProvider

class Provider(MiscProvider):
    gemstone_names: Any = ...
    mountain_names: Any = ...
    plant_names: Any = ...
    space_object_names: Any = ...
    random_object_names: Any = ...
    def gemstone_name(self): ...
    def mountain_name(self): ...
    def plant_name(self): ...
    def space_object_name(self): ...
    def random_object_name(self): ...