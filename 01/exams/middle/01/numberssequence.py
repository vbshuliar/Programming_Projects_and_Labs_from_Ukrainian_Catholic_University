def niven_numbers(length):
    lst = []
    i = 1
    while len(lst) < length:
        if i % sum(map(int, list(str(i)))) == 0:
            lst.append(i | i**3)
        i += 1
    return lst


if __name__ == "__main__":
    print(niven_numbers(16))
