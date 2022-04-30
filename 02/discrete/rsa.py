"""RSA algorithm implementation."""
import random
from prime_numbers import prime_numbers


def main(text):
    """The main function."""
    N, e, d = keys()
    encoded = encoding(text, (e, N))
    decoded = decoding(encoded, (d, N))

    print("Public keys:", (e, N))
    print("Private keys:", (d, N))
    print("Text:", text)
    print("Hash before:", hash(text))
    print("Encoded:", encoded)
    print("Decoded:", decoded)
    print("Hash after decoding:", hash(decoded))
    print("Are hashes equal:", hash(text) == hash(decoded))


def keys():
    """Generates keys."""
    temp = prime_numbers[10:20]
    p = random.choice(temp)
    temp.remove(p)
    q = random.choice(temp)

    N = p * q
    T = (p - 1) * (q - 1)

    for _ in prime_numbers:
        if _ < T and T % _ != 0 and N % _ != 0:
            e = _
            break
    d = 0
    while True:
        if (e * d) % T == 1 and d != e:
            break
        d += 1
    return N, e, d


def encoding(text, keys):
    """Encodes the message."""
    encoded = ""
    for _ in text:
        encoded += str((ord(_) ** keys[0]) % keys[1]) + " "
    return encoded


def decoding(text, keys):
    """Decodes the message."""
    decoded = ""
    for _ in text.split(" "):
        if len(_) < 1:
            continue
        decoded += str(chr((int(_) ** keys[0]) % keys[1]))
    return decoded


if __name__ == "__main__":
    main("Tests completed successfully!")
