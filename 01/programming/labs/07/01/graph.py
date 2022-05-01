"""module that calculates graph
"""


def get_graph_from_file(file_name):
    """
    (str) -> (list)

    Read graph from file and return a list of edges.

    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """

    with open(file_name, "r") as ggfl:
        result = ggfl.readlines()
        for num1 in range(len(result)):
            result[num1] = result[num1].strip().split(",")
            for num2 in range(len(result[num1])):
                result[num1][num2] = int(result[num1][num2])

    return result


def to_edge_dict(edge_list):
    """
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.

    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """

    result = {}
    for i, j in edge_list:
        result[i] = result.get(i, []) + [j]
        result[j] = result.get(j, []) + [i]

    return result


def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> bool

    Return True if graph contains a given edge and False otherwise.

    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    graph = graph.get(edge[0], []) + graph.get(edge[1], [])
    result = edge[0] in graph and edge[1] in graph
    return result


def add_edge(graph, edge):
    """
    (dict, tuple) -> dict

    Add a new edge to the graph and return new graph.

    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    if graph.get(edge[0]) is not None:
        graph.get(edge[0], []).append(edge[1])
    else:
        dkt = {edge[0]: [edge[1]]}
        graph.update(dkt)

    if graph.get(edge[1]) is not None:
        graph.get(edge[1], []).append(edge[0])
    else:
        dkt = {edge[1]: [edge[0]]}
        graph.update(dkt)

    return graph


def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)

    Delete an edge from the graph and return a new graph.

    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    try:
        if edge[0] in graph.get(edge[1]):
            temp = graph.get(edge[1])
            temp.pop(temp.index(edge[0]))           
    except (KeyError, TypeError):
        pass
    try:
        if edge[1] in graph.get(edge[0]):
            temp = graph.get(edge[0])
            temp.pop(temp.index(edge[1]))            
    except (KeyError, TypeError):
        pass

    return graph


def add_node(graph, node):
    """
    (dict, int) -> (dict)

    Add a new node to the graph and return a new graph.

    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    dkt = {node: []}
    if node not in graph:
        graph.update(dkt)

    return graph


def del_node(graph, node):
    """
    (dict, int) -> (dict)

    Delete a node and all incident edges from the graph.

    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    try:
        graph.pop(node)
    except KeyError:
        pass
    dkt = {}
    for i in graph:
        temp = graph.get(i)
        for num in range(len(temp)):
            if temp[num] == node:
                temp.pop(num)
        dkt_temp = {i: temp}
        dkt.update(dkt_temp)

    return graph


def convert_to_dot(graph):
    """
    (dict) -> (None)

    Save the graph to a file in a DOT format.
    """
    with open("dotfile.dot", "w") as dtf:
        dtf.write("graph {")
        for num1 in graph:
            for num2 in range(len(graph.get(num1))):
                temp = graph.get(num1)
                dtf.write("\n"+str(num1) + " -- " + str(temp[num2]) + ";")
        dtf.write("\n}")
