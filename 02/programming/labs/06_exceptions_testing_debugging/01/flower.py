"""Flower."""


class Flower:
    """A flower."""

    def __init__(self, petals, price, color):
        """Receives info."""
        self.petals = petals
        self.price = price
        self.color = color

    @property
    def petals(self):
        """Petals."""
        return self._petals

    @petals.setter
    def petals(self, value):
        if not isinstance(value, int):
            raise TypeError("It must be integer!")
        if value <= 0:
            raise ValueError("It's impossible!")
        self._petals = value

    @property
    def color(self):
        """Color."""
        return self._color

    @color.setter
    def color(self, value):
        if not isinstance(value, str):
            raise TypeError("It must be string!")
        self._color = value

    @property
    def price(self):
        """Price."""
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise TypeError("It must be integer!")
        if value <= 0:
            raise ValueError("It's impossible!")
        self._price = value


class Tulip(Flower):
    """Tulip."""

    def __init__(self, petals, price):
        super().__init__(petals, price, "pink")


class Rose(Flower):
    """Rose."""

    def __init__(self, petals, price):
        """Receives info."""
        super().__init__(petals, price, "red")


class Chamomile(Flower):
    """Chamomile."""

    def __init__(self, petals, price):
        """Receives info."""
        super().__init__(petals, price, "white")


class FlowerSet:
    """Flower set."""

    def __init__(self):
        """Receives info."""
        self.set_of_flowers = set()

    def add_flower(self, *flowers):
        """Adds flower to a set."""
        check = type(flowers[0])
        for _ in flowers:
            if not isinstance(_, check):
                raise TypeError("Different flowers prohibited!")
            self.set_of_flowers.add(_)
        return self.set_of_flowers


class Bucket:
    """Bucket of flowers."""

    def __init__(self):
        """Receives info."""
        self.bucket = set()

    def add_set(self, *sets):
        """Adds sets to a bucket."""
        for _ in sets:
            self.bucket.update(_.set_of_flowers)
        return self.bucket

    def total_price(self):
        """Calculates the price of the bucket."""
        total = 0
        for _ in list(self.bucket):
            total += _.price
        return total
