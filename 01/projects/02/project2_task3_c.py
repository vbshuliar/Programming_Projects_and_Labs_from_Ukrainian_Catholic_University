"""
archives directory or file
"""


import argparse
import os
import zipfile


def main():
    """
    main function
    """

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("src", type=str)
        parser.add_argument("dst", type=str)
        args = parser.parse_args()

        archivator(args.src, args.dst)

    except Exception as exc:
        print("Sorry, an error occured. Maybe, you did something wrong.")
        print(exc)


def archivator(source, destination):
    """
    archives file or directory
    """

    try:
        with zipfile.ZipFile(destination, "w") as dst:
            for roots, dirs, files in os.walk(source):
                for file1 in files:
                    dst.write(os.path.join(roots, file1))

    except Exception as exc:
        print("Sorry, an error occured. Maybe, you did something wrong.")
        print(exc)


if __name__ == "__main__":
    main()
