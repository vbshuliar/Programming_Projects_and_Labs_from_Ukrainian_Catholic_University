"""Testing module graph case study."""
from graph import Graph
from copy import deepcopy
from dfs import DFS_complete
from bfs import BFS_complete
from topological_sort import topological_sort
from answers import *


def read_file(path):
    """Reads file and generates graph graph."""

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

    # New graph and list for vertices generating.
    graph = Graph(True)
    data_graph = deepcopy(data)

    # Graph vertices inserting.
    for element in data:
        temp_vertex = graph.insert_vertex(element[0])
        for line in range(len(data_graph)):
            for vertex in range(len(data_graph[line])):
                if data_graph[line][vertex] == element[0]:
                    data_graph[line][vertex] = temp_vertex

    # Graph edges inserting.
    for element in data_graph:
        for vertex in element[1:]:
            if vertex:
                graph.insert_edge(element[0], vertex)

    return graph


def bfs_test(graph):
    """BFS algorithm testing."""
    test = BFS_complete(graph)
    output = [str(vertex) for vertex in test]
    assert output == bfs_answer
    print("BFS algoorythm completed successfully. Here are results:")
    print("\n".join(output))


def dfs_test(graph):
    """DFS algorithm testing."""
    test = DFS_complete(graph)
    output = [str(vertex) for vertex in test]
    assert output == dfs_answer
    print("DFS algoorythm completed successfully. Here are results:")
    print("\n".join(output))


def topological_sort_test(graph):
    """Topolocial sort testing."""
    test = topological_sort(graph)
    output = [str(vertex) for vertex in test]
    assert output == topological_sorting_answer
    print("Topological sorting completed successfully. Here are results:")
    print("\n".join(output))


if __name__ == "__main__":
    print("Enter path to text file:")
    path = "02/programming/labs/12/01_graph_map_testing/stanford_cs.txt"
    path = input(">>> ")
    graph = read_file(path)
    dfs_test(graph)
    print()
    bfs_test(graph)
    print()
    topological_sort_test(graph)
