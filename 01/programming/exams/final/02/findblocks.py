def find_sentences_block(path: str):
    """
    Finds sentences block.
    >>> find_sentences_block("Nestayko_sents.txt")
    (23, 24, 25, 26, 27, 28, 29, 31)
    """

    res = []
    with open(path, "r") as text:
        data = text.readlines()
    for each in data:
        temp_res = []
        temp = each.rstrip().split(" ")
        for word in temp:
            if word.isalpha():
                temp_res.append(word)
        res.append(temp_res)
    # we cleared each sentence from punctuation
    max_len = 0
    for each in res:
        if len(each) > max_len:
            max_len = len(each)
    # we found sentence with maximum length
    dct = {}
    for count in range(1, max_len + 1):
        for each in res:
            if len(each) == count:
                if count in dct.keys():
                    dct[count] = dct[count] + 1
                else:
                    dct[count] = 1
    # we counted amount of sentences with common amount of words
    lst = []
    dups = list(dct.items())
    for ind, each in enumerate(dups):
        temp = (each[0], each[1] // each[0])
        if temp[1] > 0:
            lst.append(temp)
    # we counted amount of block for each n
    duplicates = []
    for each in lst:
        counter = 0
        for num in lst:
            if each[1] == num[1] and each[0] not in duplicates:
                counter += 1
        if counter > 1:
            duplicates.append(each[0])
    # we counted duplicates
    return tuple(duplicates)


if __name__ == "__main__":
    print(find_sentences_block("Nestayko_sents.txt"))
