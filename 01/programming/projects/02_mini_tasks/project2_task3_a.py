"""
archives directory or file to destination
"""


import argparse
import zipfile
import re
import os


def main():
    """
    main function
    """

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("pattern", type=str)
        parser.add_argument("src", type=str)
        parser.add_argument("dst", type=str)
        args = parser.parse_args()
        mover(args.pattern, args.src, args.dst)

    except Exception as exc:
        print("Sorry, an error occured. Maybe, you did something wrong.")
        print(exc)


def mover(pattern, source, destination):
    """
    moves the file or directory
    """

    try:
        name = os.path.basename(source)
        abs_source = os.path.abspath(source)

        with zipfile.ZipFile(source, "r") as src:
            with zipfile.ZipFile(destination, "w") as dst:
                all_files = src.namelist()
                n = 1
                while os.path.isdir("temporary_directory"+str(n)):
                    n += 1
                os.mkdir("temporary_directory"+str(n))
                os.chdir("temporary_directory"+str(n))
                temp_dir = os.getcwd()
                for num1 in all_files:
                    if re.search(pattern, num1):
                        src.extract(num1, temp_dir)
                        dst.write(num1)

        for root, dirs, files in os.walk(temp_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.chdir("..")
        os.rmdir(temp_dir)

    except Exception as exc:
        print("Sorry, an error occured. Maybe, you did something wrong.")
        print(exc)


if __name__ == "__main__":
    main()
