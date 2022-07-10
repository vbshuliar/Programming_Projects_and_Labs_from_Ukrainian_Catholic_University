"""Unittests."""

from unittest import TestCase
import unittest
from square_preceding import *


class TestSquare(TestCase):
    """Unittests for test square precedings."""

    def test_empty(self):
        """Tests if list is empty."""
        L = []
        square_preceding(L)
        self.assertEqual(L, [])

    def test_default(self):
        """Default test."""
        L = [3, 4, 5]
        square_preceding(L)
        self.assertEqual(L, [0, 9, 16])


if __name__ == "__main__":
    unittest.main()
