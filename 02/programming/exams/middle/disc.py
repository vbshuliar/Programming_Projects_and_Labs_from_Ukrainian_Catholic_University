"""Disc module."""
import math


class Disc:
    """Disc."""

    def __init__(self, center, radius):
        """Receives information."""
        self.center = center if isinstance(center, tuple) else center.coords
        self.radius = radius

    def __repr__(self):
        """Representation of the class object."""
        x, y = self.center
        r = format(self.radius**2, ".2f")

        if x == 0:
            x_str = f"(x)**2"
        elif x > 0:
            x = format(x, ".2f")
            x_str = f"(x-{x})**2"
        else:
            x = format(x, ".2f")
            x_str + f"(x+{x})**2"

        if y == 0:
            y_str = f"(y)**2"
        elif y > 0:
            y = format(y, ".2f")
            y_str = f"(y-{y})**2"
        else:
            y = format(y, ".2f")
            y_str + f"(y+{y})**2"

        return f"{x_str} + {y_str} = {r}"

    def is_touching(self, near):
        """Checks whether discs are touching each other."""
        x1, y1 = self.center
        x2, y2 = near.center
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        print(distance)
        print(self.radius + near.radius)

        if distance < abs(self.radius - near.radius):
            return False
        if distance == 0 and self.radius == near.radius:
            return False
        if distance >= self.radius + near.radius:
            return True

    def inscribe_discs(self):
        """Inscribes discs."""
        new_x1 = self.center[0] - 0.5 * self.radius
        new_x2 = self.center[0] + 0.5 * self.radius

        new_disc1 = Disc((new_x1, self.center[1]), self.radius * 0.5)
        new_disc2 = Disc((new_x2, self.center[1]), self.radius * 0.5)

        return new_disc1, new_disc2

    def transform_disc(self, num):
        """Transforms disc."""
        self.radius += num

    def transformed_disc(self, num):
        """Transformed disc."""
        a = Disc(self.center, self.radius).transform_disc(num)
        return a


class Center:
    """Center of the disc."""

    def __init__(self, x, y):
        """Receives information."""
        self.coords = (x, y)

    def __repr__(self):
        """Representation of center."""
        return f"Center is x={self.coords[0]}, y={self.coords[1]}"
