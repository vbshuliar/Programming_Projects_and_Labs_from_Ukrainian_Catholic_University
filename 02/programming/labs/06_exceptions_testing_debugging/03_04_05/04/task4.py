"""Task 4."""

from task4_exceptions import *


class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = "film.txt"

    def insert(self, character):
        if not hasattr(character, "character"):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        try:
            del self.characters[self.cursor.position]
        except IndexError:
            raise WrongCursor("Character does not exist.")

    def save(self):
        try:
            with open(self.filename, "w") as f:
                f.write("".join(self.characters))
        except FileNotFoundError:
            raise WrongRoot("File cannot be created.")

    @property
    def string(self):
        return "".join((str(c) for c in self.characters))


class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1
        if self.position > len(self.document.characters):
            raise WrongCursor("Already at the end.")

    def back(self):
        self.position -= 1
        if self.position < 0:
            raise WrongCursor("Already at the beginning.")

    def home(self):
        try:
            while self.document.characters[self.position - 1].character != "\n":
                self.position -= 1
                if self.position == 0:
                    break
        except IndexError:
            raise WrongHome("Already at the beginning.")

    def end(self):
        while (
            self.position < len(self.document.characters)
            and self.document.characters[self.position] != "\n"
        ):
            self.position += 1


class Character:
    def __init__(self, character, bold=False, italic=False, underline=False):
        try:
            assert len(character) == 1
        except AssertionError:
            raise WrongInput("Incorrect input")
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        bold = "*" if self.bold else ""
        italic = "/" if self.italic else ""
        underline = "_" if self.underline else ""
        return bold + italic + underline + self.character


if __name__ == "__main__":
    d = Document()
    d.insert("h")
    d.insert("e")
    d.insert(Character("1", bold=True))
    d.insert(Character("1", bold=True))
    d.insert("o")
    d.insert("\n")
    d.insert(Character("w", italic=True))
    d.insert(Character("o", italic=True))
    d.insert(Character("r", underline=True))
    d.insert("l")
    d.insert("d")
    print(d.string)
    d.cursor.home()
    d.delete()
    d.insert("W")
    print(d.string)
    d.characters[0].underline = True
    print(d.string)
