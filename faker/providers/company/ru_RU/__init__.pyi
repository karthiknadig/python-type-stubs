from typing import Any

from faker.utils.datetime_safe import datetime as datetime

from .. import Provider as CompanyProvider

def calculate_checksum(value: Any): ...

class Provider(CompanyProvider):
    formats: Any = ...
    company_prefixes: Any = ...
    company_suffixes: Any = ...
    large_companies: Any = ...
    catch_phrase_adj: Any = ...
    catch_phrase_nouns_masc: Any = ...
    catch_phrase_nouns_fem: Any = ...
    catch_phrase_nouns_neu: Any = ...
    bsWords: Any = ...
    def catch_phrase(self): ...
    def large_company(self): ...
    def company_prefix(self): ...
    def businesses_inn(self): ...
    def individuals_inn(self): ...
    def businesses_ogrn(self): ...
    def individuals_ogrn(self): ...
    def kpp(self): ...