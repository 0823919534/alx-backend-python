#!/usr/bin/env python3
"""Module containing utility functions for accessing nested maps."""

from typing import Any, Mapping

def access_nested_map(nested_map: Mapping, path: tuple) -> Any:
    """Access a nested map using a sequence of keys in path."""
    current = nested_map
    for key in path:
        current = current[key]
    return current
