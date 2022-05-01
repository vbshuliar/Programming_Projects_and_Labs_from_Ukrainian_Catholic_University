def read_file(path):
    """ Return list of lines from file
    """

    result = []

    with open(path, "r", encoding="utf-8", errors='ignore') as f:
        result = f.readlines()

    return result


def country_dict(lines_list, year):
    """ Return dict from list of lines with the country as key and
    name as a value in that year
    """

    result = []
    dct1 = {}
    dct2 = {}

    lines_list = lines_list[14:]

    for i in lines_list:
        i = i.strip().replace('\t', '')
        if "}" in i:
            country = i[i.find("}") + 1:]
        else:
            country = i[i.find(")") + 1:]
        film_name = i[:i.find('(') - 1]
        year = i[i.find('(') + 1:i.find(')')]

        if year.isdigit():
            year = int(year)

        result.append([film_name, country, year])

    for i in result:
        if i[2] in dct2.keys():
            if i[1] in dct1.keys():
                dct1[i[1]].append(i[0])
            else:
                dct1[i[1]] = [i[0]]
        else:
            dct2
            if i[1] in dct1.keys():
                dct1[i[1]].append(i[0])
            else:
                dct1[i[1]] = [i[0]]

    for i in result:
        if i[2] in dct2.keys():
            dct2[i[2]].append()
        else:
            dct1[i[1]] = [i[0]]

    return dct1['USA']


def country_num(dict_country):
    """ Return sorted by the number of films list of tuples
    that each consists country and number of films
    """
    pass


def write_films(film_list):
    """ Write country and number of films to file
    """
    pass


def films_year(year=2019):
    """ Find countries and write to file
    """
    pass


if __name__ == "__main__":
    print(country_dict((read_file(
        r"/Users/macbookpro/OneDrive/ucu/programming/labs_codes/13/countries.list")), 2008))
