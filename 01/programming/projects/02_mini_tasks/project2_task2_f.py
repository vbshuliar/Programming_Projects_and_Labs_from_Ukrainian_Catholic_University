"""
finds regex in files in directory
"""


import argparse
import os
import re


def main():
    """
    main function
    """

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--show_lines", action="store_true")
        parser.add_argument("--only_show_counts", action="store_true")
        parser.add_argument("regex", type=str)
        parser.add_argument("pattern", type=str)
        args = parser.parse_args()

        if args.show_lines and args.only_show_counts:
            return print("Error. Please, use only one option")

        dct = files_filter(args.pattern, args.regex)

        if args.show_lines:
            for key in dct:
                print(key)
                for element in dct[key]:
                    print(f"{element[0]}: {element[1]}")
        elif args.only_show_counts:
            for key in dct:
                print(key)
                counter = 0
                for element in dct[key]:
                    counter += 1
                print(counter)
        else:
            for key in dct:
                print(key)
                for element in dct[key]:
                    print(element[1])

    except Exception as exc:
        print("Sorry, an error occured. Maybe, you did something wrong.")
        print(exc)


def files_filter(regex, pattern):
    """
    finds files with regex in name
    """

    filtered_files = []
    dct = {}

    try:
        for roots, dirs, files_list in os.walk(os.getcwd()):
            for file1 in files_list:
                if re.search(pattern, file1):
                    with open(file1, "r", encoding="utf-8") as file2:
                        text = file2.readlines()
                        for index, element in enumerate(text):
                            if re.search(regex, element):
                                if file1 in dct:
                                    dct[file1].append(
                                        (index + 1, element.rstrip()))
                                else:
                                    dct[file1] = [
                                        (index + 1, element.rstrip())]

    except Exception as exc:
        print("Sorry, an error occured. Maybe, you did something wrong.")
        print(exc)

    return dct


if __name__ == "__main__":
    main()
