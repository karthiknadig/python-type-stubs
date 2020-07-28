from typing import Any

class InfinityType:
    def __hash__(self) -> int: ...
    def __lt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __neg__(self) -> NegativeInfinityType: ...

Infinity: Any

class NegativeInfinityType:
    def __hash__(self) -> int: ...
    def __lt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __neg__(self) -> InfinityType: ...

NegativeInfinity: Any