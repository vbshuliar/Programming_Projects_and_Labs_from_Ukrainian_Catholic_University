"""Unittests."""

from unittest import TestCase
import unittest
from flower import *


class TestFlower(TestCase):
    """Unittests."""

    def test_default(self):
        """Tests flower."""
        self.assertTrue(isinstance(Flower(20, 30, "white"), Flower))
        self.assertTrue(isinstance(Tulip(10, 15), Tulip))
        self.assertTrue(isinstance(Rose(13, 14), Rose))
        self.assertTrue(isinstance(Chamomile(3, 4), Chamomile))

        sunflower1 = Flower(20, 10, "white")
        sunflower2 = Flower(50, 8, "black")
        tulip1 = Tulip(3, 5)
        tulip2 = Tulip(4, 6)

        a = FlowerSet()
        a.add_flower(tulip1, tulip2)
        b = FlowerSet()
        b.add_flower(sunflower1, sunflower2)
        c = Bucket()
        c.add_set(a, b)
        d = c.total_price()
        self.assertEqual(29, d)

    def test_wrong_input(self):
        """Tests flower."""
        with self.assertRaises(TypeError):
            Flower("20", 30, "white")
            Flower(20, "30", "white")
            Flower(20, 30, 1)
            a = FlowerSet()
            a.add_flower(Rose(20, 30), Tulip(10, 15))

        with self.assertRaises(ValueError):
            Flower(20, -1, "white")
            Flower(-1, 20, "white")


if __name__ == "__main__":
    unittest.main()
