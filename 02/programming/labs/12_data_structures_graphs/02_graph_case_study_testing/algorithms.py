"""
File: algorithms.py

Graph processing algorithms
"""

from linkedstack import LinkedStack


def topoSort(g, startLabel=None):
    """Topological sorting."""
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.vertices():
        if not v.isMarked():
            dfs(g, v, stack)
    return stack


def dfs(g, v, stack):
    """DFS recursive."""
    v.setMark()
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs(g, w, stack)
    stack.push(v)


def DFS_complete(g, startLabel=None):
    """DFS algorithm."""
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.vertices():
        if not v.isMarked():
            dfs(g, v, stack)
    return stack


def bfs(g, v, stack):
    """DFS recursive."""
    v.setMark()
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            stack.push(w)
            w.setMark()
    bfs(g, list(stack[-1]), stack)


def BFS_complete(g, startLabel=None):
    """DFS algorithm."""
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.vertices():
        if not v.isMarked():
            bfs(g, v, stack)
    return stack
