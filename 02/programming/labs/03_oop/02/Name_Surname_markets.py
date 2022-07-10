"""Markets class."""


class Markets():
    """Class for markets."""

    def __init__(self, name, area, categories):
        """
        Information about market.
        >>> market_family_food = Markets('Family Food',\
                                 80,\
                                 ['Bread and Bakery',\
                                  'Dairy',\
                                  'Beverages'])
        >>> market_family_food.name
        'Family Food'
        """
        self.name = name
        self.area = area
        self.categories = categories

    def __str__(self):
        """
        Brief information about market.
        >>> market_family_food = Markets('Family Food',\
                                 80,\
                                 ['Bread and Bakery',\
                                  'Dairy',\
                                  'Beverages'])
        >>> print(market_family_food)
        Supermarket Family Food has an area of 80 m2 \
and has the following categories: Bread and Bakery, Dairy, Beverages.
        """
        return f"Supermarket {self.name} has an area of {self.area}\
 m2 and has the following categories: {', '.join(self.categories)}."


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
