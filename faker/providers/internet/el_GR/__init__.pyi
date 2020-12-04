from typing import Any

from faker.utils.decorators import slugify_domain as slugify_domain

from .. import Provider as InternetProvider

class Provider(InternetProvider):
    free_email_domains: Any = ...
    tlds: Any = ...
    def user_name(self): ...
    def domain_word(self): ...

def remove_accents(value: Any): ...
def latinize(value: Any): ...