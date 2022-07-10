"""Testing module graph case study."""
from graph import LinkedDirectedGraph
from copy import deepcopy
from algorithms import *
from answers import *


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


def bfs_test(graph):
    """BFS algorythm testing."""
    test = [str(vertex) for vertex in BFS_complete(graph)]
    print("\n".join(test))


def dfs_test(graph):
    """BFS algorythm testing."""
    test = [str(vertex) for vertex in DFS_complete(graph)]
    assert test == dfs_answer
    print("DFS algorithm completed successfully. Here are results:")
    print("\n".join(test))


def topological_sort_test(graph):
    """Topolocial sort testing."""
    test = [str(vertex) for vertex in topoSort(graph)]
    assert test == topological_sorting_answer
    print("Topological sorting completed successfully. Here are results:")
    print("\n".join(test))


if __name__ == "__main__":
    test = read_file(
        "/Users/macbookpro/Library/CloudStorage/OneDrive-Personal/ucu/python/02/programming/labs/12/02_graph_case_study_testing/stanford_cs.txt"
    )
    topological_sort_test(test)
    dfs_test(test)
