def read_crossword(path):
    lst = []
    with open(path, "r") as f:
        temp = f.readlines()
        for i in range(0, len(temp), 2):
            coords = temp[i + 1].rstrip()
            while len(coords) >= 2:
                lst.append((temp[i].rstrip(), tuple(
                    list(map(int, coords[:2])))))
                coords = coords[2:]
    return lst


def crossword_words(crossword):
    lst = []
    for j in crossword:
        temp = [j]
        for j2 in crossword:
            if j[1][0] == j2[1][0] and j != j2:
                temp.append(j2)
        if len(temp) > 2:
            temp.sort(key=lambda x: x[1][1])
            word = ""
            for i in temp:
                word += i[0]
            lst.append(word)
    return list(set(lst))


if __name__ == "__main__":
    print(crossword_words(read_crossword(r"08/crossword_1_2.txt")))
    # print(read_crossword(r"08/crossword_1_2.txt"))
