"""female and male names
"""


def common_names(female_names, male_names):
    """creates new list of names
    >>> common_names(['Mary', 'Gerry'], ['Sam', 'Gerry', 'Joe'])
    set()
    """
    female = female_names
    male = male_names
    female = set(female)
    male = set(male)
    together = female & male
    together = list(together)
    output = []
    for checker in range(len(together)):
        if together[checker][:1] in "AOUIE":
            output.append(together[checker])
    return set(output)


def names_read(file_name):
    """reads file
    """
    with open(file_name, "r") as fln:
        all_names = fln.readlines()
    for num1 in range(len(all_names)):
        all_names[num1] = all_names[num1][:-1]
    return all_names
