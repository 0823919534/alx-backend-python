#!/usr/bin/env python3
"""Utilities for accessing values inside nested mapping structures."""

from typing import Any, Mapping


def access_nested_map(nested_map: Mapping, path: tuple) -> Any:
    """Retrieve the object found by walking `path` through `nested_map`.

    Each element of `path` is used as a key into the current mapping. If at any
    point the required key does not exist, or the current value is not a
    mapping while there are still keys to consume, a KeyError is raised with
    the missing key as its message.
    """
    current = nested_map
    for key in path:
        # If current is not a mapping, we cannot proceed
        if not isinstance(current, Mapping):
            raise KeyError(key)
        if key not in current:
            raise KeyError(key)
        current = current[key]
    return current

