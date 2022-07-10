"""Game."""


class Item:
    """Item."""

    def __init__(self, name):
        """
        Receives information.
        """
        self.name = name

    def set_description(self, description):
        """
        Description of the room.
        """
        self.description = description

    def describe(self):
        """
        Returns brief description.
        """
        if type(self) == Item:
            return print(f"The [{self.name}] is here - {self.description}")
        else:
            return print(f"{self.name} is here!\n{self.description}")

    def get_name(self):
        """
        Gets name.
        """
        return self.name


class Room(Item):
    """Room."""

    def __init__(self, name):
        """
        Receives information.
        """
        super().__init__(name)
        self.item = None
        self.character = None
        self.sides = []

    def link_room(self, room, side):
        """
        Links rooms.
        >>> kitchen = Room("Kitchen")
        >>> bedroom = Room("Bedroom")
        >>> kitchen.link_room(bedroom, "south")
        >>> kitchen.sides[0][0]
        'Bedroom'
        """
        if side in ["south", "west", "east", "north"]:
            self.sides.append([room.name, side, room])
        else:
            return print("No such side.")

    def get_details(self):
        """
        Returns brief details abot the room.
        """
        self.rooms = ""
        for _ in self.sides:
            self.rooms += "The " + _[0] + " is " + _[1]
            if _ != self.sides[-1]:
                self.rooms += "\n"
        return print(
            f"""\n
{self.name}
--------------------
{self.description}
{self.rooms}"""
        )

    def set_character(self, character):
        """
        Sets character.
        """
        self.character = character

    def get_character(self):
        """
        Returns character from the room.
        """
        return self.character

    def set_item(self, item):
        """
        Sets item.
        """
        self.item = item

    def get_item(self):
        """
        Returns item in the room.
        """
        return self.item

    def move(self, decision):
        """
        Moves to wanted room.
        """
        for _ in self.sides:
            if _[1] == decision:
                return _[2]


class Person(Item):
    """Person."""

    def __init__(self, name, description):
        """
        Receives information.
        """
        super().__init__(name)
        self.set_description(description)

    def set_conversation(self, conversation):
        """
        Sets conversation.
        """
        self.conversation = conversation

    def talk(self):
        """
        Talk with somebody.
        """
        return print(f"[{self.name} says]: {self.conversation}")


class Enemy(Person):
    """Enemy."""

    def __init__(self, name, description):
        """
        Receives information.
        """
        super().__init__(name, description)
        self.defeated = 0

    def set_weakness(self, weakness):
        """
        Sets weakness.
        """
        self.weakness = weakness

    def fight(self, weapon):
        """
        Starts fight with an enemy.
        """
        if self.weakness == weapon:
            return True
            self.defeated += 1

    def get_defeated(self):
        """
        Gets defeated.
        """
        return self.defeated


class Friend(Person):
    """Friend. Just wishes a good day."""

    def __init__(self, name, conversation):
        """
        Receives information.
        """
        super().__init__(name)
        self.set_conversation(conversation)


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
