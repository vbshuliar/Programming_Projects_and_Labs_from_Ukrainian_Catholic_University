"""Testing module graph case study."""
from graph import Graph


def main():
    """The main function."""
    pass


def read_file(path):
    """Reads file."""
    text = []
    with open(path, "r", encoding="UTF-8") as data:
        for _ in data.readlines():
            if not _.startswith("#"):
                temp = _[:-1].split(" ")
                for _ in range(len(temp)):
                    temp[_] = temp[_].replace("(", "").replace(")", "")
                text.append(temp)
    
    


def bfs_test():
    """BFS algorythm testing."""
    pass


def dfs_test():
    """BFS algorythm testing."""
    pass


def topological_sort_test():
    """Topolocial sort testing."""
    pass


if __name__ == "__main__":
    a = read_file("02/programming/labs/12/stanford_cs.txt")
    for _ in a:
        print(_)
