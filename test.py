import functools
import inspect
from enum import Enum,IntEnum


class EnumClass(Enum):
    ENTRY = 0
    def ok(self):
        return self.value
    def __repr__(self):
        return ok
print(EnumClass.ENTRY.ok())