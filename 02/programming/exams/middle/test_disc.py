"""Tests."""

from unittest import TestCase
import unittest
from disc import *


class TestDisc(TestCase):
    """Tests for disc."""

    def test_default(self):
        """All the tests."""
        a = Disc(Center(1, 1), 3)

        assert str(Disc(Center(1, 1), 3)) == "(x-1.00)**2 + (y-1.00)**2 = 9.00"
        assert str(Disc(Center(5, 5), 4)) == "(x-5.00)**2 + (y-5.00)**2 = 16.00"
        assert str(Disc(Center(0, 3), 1)) == "(x)**2 + (y-3.00)**2 = 1.00"
        assert str(Disc(Center(0, 0), 2)) == "(x)**2 + (y)**2 = 4.00"
        assert str(Disc(Center(0, 1), 1)) == "(x)**2 + (y-1.00)**2 = 1.00"
        assert str(Disc(Center(1, 4), 1)) == "(x-1.00)**2 + (y-4.00)**2 = 1.00"

        assert str(Center(1, 4)) == "Center is x=1, y=4"

        disc1 = Disc(Center(1, 1), 3)
        assert str(disc1) == "(x-1.00)**2 + (y-1.00)**2 = 9.00"
        assert disc1.radius == 3
        assert isinstance(disc1.radius, int)
        assert disc1.center == (1, 1)

        disc2 = Disc(Center(5, 5), 4)
        assert str(disc2) == "(x-5.00)**2 + (y-5.00)**2 = 16.00"
        assert disc2.radius == 4
        assert disc2.center == (5, 5)

        assert not disc1.is_touching(disc2)

        (disc5, disc6) = disc2.inscribe_discs()
        assert str(disc5) == "(x-3.00)**2 + (y-5.00)**2 = 4.00"
        assert str(disc6) == "(x-7.00)**2 + (y-5.00)**2 = 4.00"
        assert disc5.is_touching(disc6)
        disc2.transform_disc(2)
        assert str(disc2) == "(x-5.00)**2 + (y-5.00)**2 = 36.00"
        disc2.transform_disc(-2)
        assert str(disc2) == "(x-5.00)**2 + (y-5.00)**2 = 16.00"
        disc = disc2.transformed_disc(2)


if __name__ == "__main__":
    unittest.main()
