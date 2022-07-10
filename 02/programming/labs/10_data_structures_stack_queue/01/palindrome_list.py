"""Palindrome."""
from arraystack import ArrayStack


class Palindrome:
    """Palindrome."""

    def __init__(self, words=[]):
        """Initializes object of the class."""
        self.words = words

    def is_palindrome(self, word):
        """Checks whether word is a palindrome."""
        temp = ArrayStack(word[: len(word) // 2])
        for _ in range(len(word) // 2):
            if temp.peek() != word[_ - len(word) // 2]:
                return False
            temp.pop()
        return True

    def read_file(self, path):
        """Reads file."""
        with open(path, "r", encoding="UTF-8") as words:
            data = words.readlines()
            for _ in range(len(data)):
                if data[_].startswith(" +cs="):
                    data[_] = data[_][5:]
                data[_] = data[_][: data[_].find(" ")]

        return data

    def write_to_file(self, path, words):
        """Writes polindromes."""
        with open(path, "w", encoding="UTF-8") as new:
            new.write("\n".join(words))

    def find_palindromes(self, start, finish):
        """Checks for polindromes."""
        result = []
        for _ in self.read_file(start):
            if self.is_palindrome(_) and len(_) > 0:
                result.append(_)
        print(result)
        self.write_to_file(finish, result)
        return result
