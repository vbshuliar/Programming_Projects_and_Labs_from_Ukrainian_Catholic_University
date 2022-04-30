"""
finds films by keywords
"""


def find_film_keywords(film_keywords, film_name):
    """
    finds keywords from film
    >>> find_film_keywords({'a': ['mom', 'dad', 'baby'], 'b':\
 ['mom', 'dad'], 'c': ['mom', 'dad'], 'd': \
['mom', 'dad'], 'e': ['mom', 'dad'], 'f': ['mom', 'dad']}, 'baby')
    {'a'}
    """

    result = []

    for num1 in film_keywords:
        keyword = film_keywords[num1]
        for num2 in range(len(keyword)):
            if keyword[num2] == film_name:
                result.append(num1)

    return set(result)


def find_films_with_keywords(film_keywords, num_of_films):
    """
    finds film with keywords
    >>> find_films_with_keywords({'a': ['mom', 'dad', 'baby'], 'b':\
 ['mom', 'dad'], 'c': ['mom', 'dad'], 'd': \
['mom', 'dad'], 'e': ['mom', 'dad'], 'f': ['mom', 'dad']}, 2)
    [('mom', 6), ('dad', 6)]
    """

    result = {}

    for num1 in film_keywords:
        for num2 in film_keywords.get(num1):
            if num2 not in result:
                result[num2] = 1
            else:
                result[num2] = result[num2] + 1

    output = list(result.items())
    output.sort(key=lambda x: x[1], reverse=True)

    return output[:num_of_films]
