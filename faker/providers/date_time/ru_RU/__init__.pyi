from typing import Any

from .. import Provider as DateTimeProvider

class Provider(DateTimeProvider):
    DAY_NAMES: Any = ...
    MONTH_NAMES: Any = ...
    countries: Any = ...
    def day_of_week(self): ...
    def month_name(self): ...
