"""Letters module."""


class First:
    """The first class."""

    all_vowels = ["i", "a", "u", "o", "u", "y", "e"]

    def __init__(self, word):
        """Receives information."""
        self.word = word
        self.vowels = []
        self.consonants = []
        for letter in word:
            if letter in self.all_vowels:
                self.vowels.append(letter)
            else:
                self.consonants.append(letter)

    def __str__(self):
        """Brief representation of a class object."""
        return f"First(consonants={self.consonants}, vowels={self.vowels})"

    def __eq__(self, another):
        """Equality check."""
        if type(self) != type(another):
            return False
        if self.consonants == another.consonants:
            return True
        return False

    def clear_vowels(self):
        """Clears vowels from the word."""
        self.vowels = []

    def cleared_vowels(self):
        """Return copy of the object but with cleared vowels."""
        return First("".join(self.consonants))


class Second(First):
    """The second class that inherits the first one."""

    def __init__(self, word, shift):
        """Receives information."""
        self.__shift = shift
        super().__init__(word)

    def encoder(self):
        """Encodes the word with a shift."""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        new_word = ""
        for letter in self.consonants:
            new_word += alphabet[(alphabet.index(letter) + self.__shift) % 26]
        for letter in self.vowels:
            new_word += alphabet[(alphabet.index(letter) + self.__shift) % 26]
        return Second(new_word, 5)
