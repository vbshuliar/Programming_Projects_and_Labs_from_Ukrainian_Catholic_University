"""
my tasks
"""


def get_number():
    # takes user's personal code
    number = 90
    return number


# ****************************************
# Problem 5
# ****************************************
def type_by_sides(a, b, c):
    '''
    (float, float, float) -> str
    Detect the type of triangle by it's sides and return type as string
    ('right angled triangle', 'obutuse triangle', 'acute triangle'). If there is no
    triangle with such sides, then function should return None.

    >>> type_by_sides(3, 3, 3)
    'acute triangle'
    >>> type_by_sides(3, 4, 5)
    'right angled triangle'
    >>> type_by_sides(3, 3, 2015)
    None
    >>> type_by_sides(4, 3, 6)
    'obutuse triangle'
    '''

    if a == b == c:
        return 'acute triangle'
    elif a**2+b**2 == c**2 or b**2+c**2 == a**2 or a**2+c**2 == b**2:
        return 'right angled triangle'
    elif a+b < c or a+c < b or b+c < a:
        return None
    else:
        return 'obutuse triangle'


# ****************************************
# Problem 7
# ****************************************
def convert_to_column(s):
    '''
    str -> str
    Convert string to a column of words.
    If argument is not a string function should return None.

    >>> print_column('Revenge is a dish that tastes best when served cold.')
    revenge
    is
    a
    dish
    that
    tastes
    best
    when
    served
    cold
    >>> print_column('Never hate your enemies. It affects your judgment.')
    never
    hate
    your
    enemies
    it
    affects
    your
    judgment
    >>> print_column(2015)
    None
    '''
    result = ""
    punc = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
    if type(s) != str:
        return None
    s = s.lower().split(" ")
    for num1 in s:
        for num2 in num1:
            if num2 in punc:
                num1 = num1.replace(num2, "")
        result += f"{num1}\n"
    return result.rstrip()


# ****************************************
# Problem 12
# ****************************************
def exclude_letters(s1, s2):
    '''
    (str, str) -> str
    Delete all letter from string s2 in string s1. If arguments aren't strings function should
    return None.

    >>> exclude_letters('aaabb', 'b')
    'aaa'
    >>> exclude_letters('abcc', 'cczzyy')
    'ab'
    >>> exclude_letters(2015, 'sasd')
    None
    '''
    if type(s1) is not str and type(s1) is not str:
        return None
    for i in s1:
        if i in s2:
            s1 = s1.replace(i, "")
    return s1


# ****************************************
# Problem 13
# ****************************************
def create_string(lst):
    '''
    list -> str
    Create and return string from histogrma of letters. If argument isn't list of 26 positive
    integer numbers function should return None.

    >>> create_string([0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    bcc
    >>> create_string([4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]])
    aaaazzzz
    >>> create_string([4, 0, 0, 0, 0, 0])
    None
    '''
    eng = "abcdefghijklmnopqrstuvwxyz"
    result = ''
    if len(lst) != 26:
        return None
    for index in range(len(eng)):
        result += eng[index]*lst[index]
    return result


# ****************************************
# Problem 15
# ****************************************
def find_intersection(s1, s2):
    '''
    (str, str) -> str
    Find and returs string of all letters in alphabetic order that
    are present in both strings. If arguments aren't strings function
    should return None.

    >>> find_intersection('aaabb', 'bbbbccc')
    b
    >>> find_intersection('aZAbc', 'zzYYxp')
    z
    >>> find_intersection('sfdfsdf', 2015)
    None
    '''
    if type(s1) is not str or type(s2) is not str:
        return None
    eng = "abcdefghijklmnopqrstuvwxyz"
    s1 = s1.lower()
    s2 = s2.lower()
    result = ""
    for i in eng:
        if i in s1 and i in s2:
            result += i
    return result


# ****************************************
# Problem 16
# ****************************************
def find_union(s1, s2):
    '''
    (str, str) -> str
    Find and return string of all letters in alphabetic order that
    are present in either strings. If arguments aren't strings function should
    return None.

    >>> find_union('aaabb', 'bbbbccc')
    abc
    >>> find_union('aZAbc', 'zzYYxp')
    AYZabcpxz
    >>> find_union('sfdfsdf', 2015)

    '''
    if type(s1) is not str or type(s2) is not str:
        return None
    eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in eng:
        if i in s1 or i in s2:
            result += i
    return result

# ****************************************
# Problem 17
# ****************************************


def number_of_occurence(lst, s):
    '''
    (list, str) -> int
    Find and return number of occurence of string s in all elements of the
    list lst. If lst isn't list of strings or s isn't string function should
    return None.

    >>> number_of_occurence(['man', 'girl', 'women', 'boy'], 'm')
    2
    >>> number_of_occurence(['ab', 'aba', 'a', 'b', 'ba'], 'ba')
    2
    >>> number_of_occurence([1, 2, 2015, 1, 3], '1')

    '''
    for i in lst:
        if type(i) is not str:
            return None
    if type(s) is not str:
        return None
    counter = 0
    for i in lst:
        if s in i:
            counter += 1
    return counter


# ****************************************
# Problem 18
# ****************************************
def number_of_capital_letters(s):
    '''
    str -> str
    Find and return number of capital letters in string. If argument isn't string
    function should return None.

    >>> number_of_capital_letters('ArithmeticError')
    2
    >>> number_of_occurence('EOFError')
    4
    >>> number_of_capital_letters(1)
    None
    '''
    eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if type(s) is not str:
        return None
    counter = 0
    for i in s:
        if i in eng:
            counter += 1
    return counter


# ****************************************
# Problem 19
# ****************************************
def polygon_area(vertices):
    '''
    >>> polygon_area([(4,10), (9,7), (11,2), (2,2)])
    45.5
    >>> polygon_area([(9,7), (11,2), (2,2), (4, 10)])
    45.5
    >>> polygon_area([(0, 0), (0.5,1), (1,0)])
    0.5
    >>> polygon_area([(0, 10), (0.5,11), (1,10)])
    0.5
    >>> polygon_area([(-0.5, 10), (0,-11), (0.5,10)])
    10.5

    '''


# ****************************************
# Problem 21
# ****************************************
def polynomials_multiply(polynom1, polynom2):
    '''
    # (2x)*(3x) == 6
    >>> polynomials_multiply([2], [3])
    [6]
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    >>> polynomials_multiply([2,-4],[3,5])
    [6,-2,-20]
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    >>> polynomials_multiply([2,0,-4],[3,0,2,0])
    [6,0,-8,0,-8,0]

    '''

    return True


# ****************************************
# Problem 22
# ****************************************
def pattern_number(sequence):
    '''
    >>> pattern_number([])
    None
    >>> pattern_number([42])
    None
    >>> pattern_number([1,2])
    None
    >>> pattern_number([1,1])
    ([1], 2)
    >>> pattern_number([1,2,1])
    None
    >>> pattern_number([1,2,3,1,2,3])
    ([1,2,3], 2)
    >>> pattern_number([1,2,3,1,2])
    None
    >>> pattern_number([1,2,3,1,2,3,1])
    None
    >>> pattern_number(list(range(10))*20)
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20)
    >>> pattern_number('мама')
    ('ма', 2)
    >>> pattern_number('барабан')
    None
    '''
    counter = 0
    for i in sequence:
        i = sequence[:i]
        for n in sequence[i:]:
            if i == n:
                continue
                counter += 1
            else:
                counter = 0
                break
        if counter > 0:
            pattern = i
    return (pattern, counter)
        
        
    


# ****************************************
# Problem 25
# ****************************************
def happy_number(n):
    '''
    >>> happy_number(32)
    True
    >>> happy_number(33)
    False
    '''

    return True
