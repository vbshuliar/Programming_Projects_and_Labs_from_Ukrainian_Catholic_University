"""
replaces text in file or outputs in console
"""


import argparse


def main():
    """
    main function
    """

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--inplace", action="store_true")
        parser.add_argument("find", type=str)
        parser.add_argument("change", type=str)
        parser.add_argument("file_route", type=str)
        args = parser.parse_args()

        if args.inplace:
            work_file(args.find, args.change, args.file_route)
        else:
            print(work_console(args.find, args.change, args.file_route))

    except Exception as exc:
        print("Sorry, an error occured. Maybe, you did something wrong.")
        print(exc)


def work_file(find, change, file_route):
    """
    rewrites file and changes text
    """

    try:
        with open(file_route, 'r', encoding='utf-8') as file1:
            file2 = file1.read()

        file2 = file2.replace(find, change)

        with open(file_route, 'w', encoding='utf-8') as file3:
            file3.write(file2)

    except Exception as exc:
        print("Sorry, an error occured. Maybe, you did something wrong.")
        print(exc)


def work_console(find, change, file_route):
    """
    changes text in file and outputs in console
    """

    try:
        with open(file_route, 'r', encoding='utf-8') as file1:
            file2 = file1.read()

        file2 = file2.replace(find, change)

    except Exception as exc:
        print("Sorry, an error occured. Maybe, you did something wrong.")
        print(exc)

    return file2


if __name__ == "__main__":
    main()
