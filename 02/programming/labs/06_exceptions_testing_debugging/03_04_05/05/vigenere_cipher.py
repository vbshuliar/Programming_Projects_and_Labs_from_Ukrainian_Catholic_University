"""Task 5."""


class VigenereCipher:
    """Vigenere cipher algorithm."""

    def __init__(self, keyword):
        """Receives info."""
        self.keyword = keyword

    def extend_keyword(self, number):
        """Extends keyword."""
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

    def encode(self, plaintext):
        """Encodes the message."""
        plaintext = clear_text(plaintext)
        cipher = []
        keyword = self.extend_keyword(len(plaintext))
        for p, k in zip(plaintext, keyword):
            cipher.append(combine_character(p, k))
        return "".join(cipher)

    def decode(self, ciphertext):
        """Decodes the message."""
        ciphertext = clear_text(ciphertext)
        plain = []
        keyword = self.extend_keyword(len(ciphertext))
        for p, k in zip(ciphertext, keyword):
            plain.append(separate_character(p, k))
        return "".join(plain)


def clear_text(text):
    """Rights the text."""
    text, temp = list(text.upper()), ""
    for _ in text:
        if _.isalpha():
            temp += _
    return temp


def combine_character(plain, keyword):
    """Combines character."""
    plain = plain.upper()
    keyword = keyword.upper()
    plain_num = ord(plain) - ord("A")
    keyword_num = ord(keyword) - ord("A")
    return chr(ord("A") + (plain_num + keyword_num) % 26)


def separate_character(cypher, keyword):
    """Separates character."""
    cypher = cypher.upper()
    keyword = keyword.upper()
    cypher_num = ord(cypher) - ord("A")
    keyword_num = ord(keyword) - ord("A")
    return chr(ord("A") + (cypher_num - keyword_num) % 26)
