"""cmudict compiler
"""


def dict_reader_tuple(file_dict):
    """returns list of tuples
    """
    with open(file_dict, "r") as fdkt:
        result = fdkt.readlines()
        for num1 in range(len(result)):
            result[num1] = result[num1].strip().split(" ")
            result[num1] = (result[num1][0], int(
                result[num1][1]), result[num1][2:])
    return result


def dict_reader_dict(file_dict):
    """returns dictionary
    """
    dkt = {}
    with open(file_dict, "r") as fdkt:
        result = fdkt.readlines()
    for num1 in range(len(result)):
        result[num1] = result[num1].strip().split(" ")
        result[num1].pop(1)
        temp_dkt = {result[num1][0]: set(tuple(result[num1][1:]))}
        if result[num1][0] in dkt:
            temp1 = tuple(dkt.get(result[num1][0]))
            temp2 = tuple(result[num1][1:])
            temp3 = temp1, temp2
            temp_dkt = {result[num1][0]: set(temp3)}
        dkt.update(temp_dkt)
    return dkt


def dict_invert(dct):
    """inverts dict
    >>> dict_invert({'WATER':{('W','A','T','E','R')}})
    {1: {('WATER', ('W','A','T','E','R'))}}
    """
    if type(dct) == dict:
        dkt = {}
        for num1 in dct:
            tempik = []
            temp_value = sorted(dct.get(num1))
            for num2 in range(len(dct.get(num1))):
                temp_res = tuple([num1, temp_value[num2]])
                tempik.append(temp_res)
            kf2 = len(tempik)
            if kf2 in dkt:
                tempor = sorted(dkt.get(kf2))
                tempor = set(tempor + tempik)
                temp_dkt = {kf2: tempor}
                dkt.update(temp_dkt)
            else:
                temp_dkt = {len(tempik): set(tempik)}
                dkt.update(temp_dkt)
    else:
        dict_invert(dict_reader_dict("cmudict.txt"))
    return dkt
