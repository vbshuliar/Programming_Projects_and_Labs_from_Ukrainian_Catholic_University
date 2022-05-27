"""Testing module graph case study."""
from graph import LinkedDirectedGraph
from copy import deepcopy
from 


def read_file(path):
    """Reads file."""

    # Text file parsing.
    data = []
    with open(path, "r") as text:
        for line in text.readlines()[1:]:
            temp = (
                line.rstrip().replace("(", "").replace(")", "").replace(",", "").split()
            )
            for vertex in range(len(temp)):
                if temp[vertex] == "none":
                    temp[vertex] = None
            data.append(temp)

    graph = LinkedDirectedGraph()

    # Graph vertices inserting.
    for element in data:
        for vertex in element:
            if not graph.containsVertex(vertex) and vertex:
                graph.addVertex(vertex)

    # Graph edges inserting.
    for element in data:
        for vertex in element[1:]:
            if vertex:
                graph.addEdge(element[0], vertex, None)

    return graph


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
    test = read_file(
        "02/programming/labs/12/02_graph_case_study_testing/stanford_cs.txt"
    )
    for _ in test.edges():
        print(_)
