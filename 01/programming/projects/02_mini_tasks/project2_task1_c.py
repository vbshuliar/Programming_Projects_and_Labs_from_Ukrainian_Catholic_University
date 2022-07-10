"""
Crypts the file with cipher
"""


import argparse


def main():
    """
    main function
    """

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--inplace", type=str)
        parser.add_argument("--decrypt", action="store_true")
        parser.add_argument("--offset", type=int, default=13)
        args = parser.parse_args()

        with open(args.inplace, "r", encoding='utf-8') as file1:
            data = file1.readlines()

        if args.decrypt:
            new_data = decryption(data, args.offset)
        else:
            new_data = encryption(data, args.offset)

        with open(args.inplace, "w", encoding='utf-8') as file2:
            file2.writelines(new_data)

    except Exception as exc:
        print("Sorry, an error occured. Maybe, you did something wrong.")
        print(exc)


def encryption(data, key):
    """
    encrypts text from file
    """

    ukr = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    ukr_bigger = ukr.upper()
    eng = "abcdefghijklmnopqrstuvwxyz"
    eng_bigger = eng.upper()
    result = []

    try:
        for num1 in range(len(data)):
            temp_res = []
            for num2 in range(len(data[num1])):
                f_letter = data[num1][num2]
                if f_letter in ukr:
                    new_letter = ukr[(ukr.find(f_letter) + key) % len(ukr)]
                    temp_res.append(new_letter)
                elif f_letter in eng:
                    new_letter = eng[(eng.find(f_letter) + key) % len(eng)]
                    temp_res.append(new_letter)
                elif f_letter in eng_bigger:
                    new_letter = eng_bigger[(eng_bigger.find(
                        f_letter) + key) % len(eng_bigger)]
                    temp_res.append(new_letter)
                elif f_letter in ukr_bigger:
                    new_letter = ukr_bigger[(ukr_bigger.find(
                        f_letter) + key) % len(ukr_bigger)]
                    temp_res.append(new_letter)
                else:
                    temp_res.append(f_letter)
            temp_res = "".join(temp_res)
            result.append(temp_res)

    except Exception as exc:
        print("Sorry, an error occured. Maybe, you did something wrong.")
        print(exc)

    return result


def decryption(data, key):
    """
    decrypts text from file
    """

    ukr = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    ukr_bigger = ukr.upper()
    eng = "abcdefghijklmnopqrstuvwxyz"
    eng_bigger = eng.upper()
    result = []

    try:
        for num1 in range(len(data)):
            temp_res = []
            for num2 in range(len(data[num1])):
                f_letter = data[num1][num2]
                if f_letter in ukr:
                    new_letter = ukr[(ukr.find(f_letter) - key) % len(ukr)]
                    temp_res.append(new_letter)
                elif f_letter in eng:
                    new_letter = eng[(eng.find(f_letter) - key) % len(eng)]
                    temp_res.append(new_letter)
                elif f_letter in eng_bigger:
                    new_letter = eng_bigger[(eng_bigger.find(
                        f_letter) - key) % len(eng_bigger)]
                    temp_res.append(new_letter)
                elif f_letter in ukr_bigger:
                    new_letter = ukr_bigger[(ukr_bigger.find(
                        f_letter) - key) % len(ukr_bigger)]
                    temp_res.append(new_letter)
                else:
                    temp_res.append(f_letter)
            temp_res = "".join(temp_res)
            result.append(temp_res)

    except Exception as exc:
        print("Sorry, an error occured. Maybe, you did something wrong.")
        print(exc)

    return result


if __name__ == "__main__":
    main()
