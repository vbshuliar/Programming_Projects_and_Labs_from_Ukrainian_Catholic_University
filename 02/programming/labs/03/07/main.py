"""Logistics module."""
from random import uniform


class Item:
    """Description for an item."""

    def __init__(self, name: str, price: float):
        """
        Receives information.
        >>> my_item = Item("Toy", 25)
        >>> my_item.name
        'Toy'
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """
        Prints brief information.
        >>> my_item = Item("Toy", 25)
        >>> print(my_item)
        The price for Toy equals 25.
        """
        return f"The price for {self.name} equals {self.price}."


class Vehicle:
    """Vehicle used for delivery."""

    def __init__(self, vehicleNo: int, isAvailable=True):
        """
        Receives information.
        >>> cars = [Vehicle(1), Vehicle(2)]
        >>> cars[0].vehicleNo
        1
        """
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable


class Location:
    """Location of delivery service."""

    def __init__(self, city: str, postoffice: int):
        """
        Receives information.
        >>> destination = Location("Lviv", 19)
        >>> destination.city
        'Lviv'
        """
        self.city = city
        self.postoffice = postoffice


class Order:
    """All the information about order and consumer."""

    def __init__(self, user_name, city, postoffice, items):
        """
        Receives information.
        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order('Oleg', 'Lviv', 53, my_items)
        """
        self.orderId = round(uniform(100000000, 999999999))
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items

    def __str__(self) -> str:
        """
        Prints brief information.
        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order('Oleg', 'Lviv', 53, my_items)
        >>> text = my_order.__str__()[:20]
        >>> print(text)
        Your order number is
        """
        return f"Your order number is {self.orderId}."

    def calculateAmount(self) -> int:
        """
        Calculates amount.
        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order('Oleg', 'Lviv', 53, my_items)
        >>> print(my_order.calculateAmount())
        154
        """
        total = 0
        for _ in self.items:
            total += _.price
        return total

    def assignVehicle(self, vehicle: Vehicle):
        """
        Assigns vehicle.
        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order('Oleg', 'Lviv', 53, my_items)
        >>> logSystem.placeOrder(my_order)
        >>> print(my_order.vehicle.vehicleNo)
        1
        """
        self.vehicle = vehicle


class LogisticSystem:
    """Database."""

    def __init__(self, vehicles: list):
        """
        Receives information.
        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> logSystem.vehicles[0].vehicleNo
        1
        """
        self.vehicles = vehicles
        self.orders = []

    def placeOrder(self, order) -> None:
        """
        Places order.
        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order('Oleg', 'Lviv', 53, my_items)
        >>> logSystem.placeOrder(my_order)
        >>> my_order2 = Order('Anton', 'Kyiv', 34, my_items)
        >>> logSystem.placeOrder(my_order2)
        >>> my_order3 = Order('Maria', 'Lviv', 32, my_items)
        >>> logSystem.placeOrder(my_order3)
        'There is no available vehicle to deliver an order.'
        """
        if len(self.vehicles) >= 1:
            order.assignVehicle(self.vehicles[0])
            self.orders.append(order)
            self.vehicles.pop(0)
        else:
            return f"There is no available vehicle to deliver an order."

    def trackOrder(self, orderId: int) -> str:
        """
        Tracks order.
        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order('Oleg', 'Lviv', 53, my_items)
        >>> logSystem.placeOrder(my_order)
        >>> logSystem.trackOrder(0)
        'No such order.'
        """
        for _ in self.orders:
            if _.orderId == orderId:
                return f"Your order #{_.orderId} is sent to {_.location.city}. Total price: {_.calculateAmount()} UAH."
        return f"No such order."


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
