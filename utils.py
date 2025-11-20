#!/usr/bin/env python3
"""Small helper utilities for memoization."""

from functools import wraps
from typing import Any, Callable

def memoize(func: Callable) -> Callable:
"""Cache the result of a no-argument instance method."""
cache_attr = "*memoized*" + func.**name**

```
@wraps(func)
def wrapper(self) -> Any:
    if not hasattr(self, cache_attr):
        setattr(self, cache_attr, func(self))
    return getattr(self, cache_attr)
return wrapper
```


