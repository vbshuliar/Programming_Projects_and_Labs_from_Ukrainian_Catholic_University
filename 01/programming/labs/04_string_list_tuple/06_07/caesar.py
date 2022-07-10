def caesar_encode(message, key):
    """encodes cipher
    (str, int) -> str
    >>> caesar_encode("abc", 1)
    'bcd'
    """
    result = ""
    temp = ""
    key = key % 26
    for i in range(len(message)):
        if ord(message[i]) + key >= 97 and ord(message[i]) + key <= 122:
            temp = message.replace(message[i], chr(ord(message[i]) + key))[i]
            result = result + temp
        elif message[i] == " ":
            result = result + " "
        elif ord(message[i]) + key > 122:
            temp = message.replace(
                message[i], chr(ord(message[i]) + key - 26))[i]
            result = result + temp
    return result


def caesar_decode(message, key):
    """decodes cipher
    (str, int) -> str
    >>> caesar_decode("bcd", 1)
    'abc'
    """
    result = ""
    temp = ""
    key = key % 26
    for i in range(len(message)):
        if ord(message[i]) - key >= 97 and ord(message[i]) - key <= 122:
            temp = message.replace(message[i], chr(ord(message[i]) - key))[i]
            result = result + temp
        elif message[i] == " ":
            result = result + " "
        elif ord(message[i]) - key < 97:
            temp = message.replace(
                message[i], chr(ord(message[i]) - key + 26))[i]
            result = result + temp
    return result


if __name__ == "__main__":
    print(caesar_encode("abc", 3))
