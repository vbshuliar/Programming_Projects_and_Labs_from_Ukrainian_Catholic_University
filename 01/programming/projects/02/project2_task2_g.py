"""
moves directory or file to destination
"""


import argparse
import os


def main():
    """
    main function
    """

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("src", type=str)
        parser.add_argument("dst", type=str)
        args = parser.parse_args()

        mover(args.src, args.dst)

    except Exception as exc:
        print("Sorry, an error occured. Maybe, you did something wrong.")
        print(exc)


def mover(source, destination):
    """
    moves the file or directory
    """

    try:
        name = os.path.basename(source)
        dst = os.path.join(destination, name)
        os.replace(source, dst)

    except Exception as exc:
        print("Sorry, an error occured. Maybe, you did something wrong.")
        print(exc)


if __name__ == "__main__":
    main()
