from .. import Provider as DateTimeProvider

class Provider(DateTimeProvider):
    def day_of_week(self): ...
    def month_name(self): ...