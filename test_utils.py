#!/usr/bin/env python3
"""Unit tests for utils.memoize."""

import unittest
from unittest.mock import patch
from utils import memoize

class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator."""

    def test_memoize(self):
        """Ensure memoize caches result and calls underlying method only once."""

        class TestClass:
            def a_method(self):
                return 42

            @property
            @memoize
            def a_property(self):
                return self.a_method()

        obj = TestClass()

        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            v1 = obj.a_property
            v2 = obj.a_property

            assert v1 == 42
            assert v2 == 42

            mock_method.assert_called_once()

if __name__ == "__main__":
    unittest.main()

