"""module sorts songs
"""


from typing import List, Tuple, Callable, Union


def song_length(argument: Tuple[str]) -> float:
    """sorts by song length
    >>> song_length(("Мало мені", "5.06"))
    5.06
    """
    return float(argument[1])


def title_length(argument: Tuple[str]) -> int:
    """sorts by title length
    >>> title_length(("Мало мені", "5.06"))
    9
    """
    return len(argument[0])


def last_word(argument: Tuple[str]) -> str:
    """sorts by last word
    >>> last_word(("Мало мені", "5.06"))
    'м'
    """
    temp = argument[0]
    if temp.count(" ") > 0:
        temp1 = temp.split(sep=" ")
        temp2 = temp1[-1][0]
    else:
        temp2 = temp[0]
    return temp2


def sort_songs(
        song_titles: List[str],
        length_songs: List[str],
        key: Callable[[tuple], Union[int, str, float]]) -> List[tuple]:
    """sorts songs
    >>> sort_songs(["Янанебібув", "Той день"], ["3.19", "3.58"], last_word)
    [('Янанебібув', '3.19'), ('Той день', '3.58')]
    """
    if len(song_titles) != len(length_songs):
        return None
    sort_list = list(zip(song_titles, length_songs))
    sort_list.sort(key=key)
    return sort_list
