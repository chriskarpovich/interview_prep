"""
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""
from graph import *
from collections import deque
import unittest
        
def is_route(graph, start, end):
    def dfs(graph, node, end, seen):
        if not node:
            return False
        # mark node as seen
        seen[node] = node
        if node == end:
            return True
        if node in graph:
            for child in graph[node]:
                if child not in seen:
                    if dfs(graph, child, end, seen):
                        return True
        return False
    seen = dict()
    return dfs(graph, start, end, seen)

def is_route_bfs(graph, start, end):
    q = deque()
    seen = dict()
    if not start or not end:
        return False
    seen[start] = start
    q.append(start)
    while q:
        node = q.popleft()
        if node == end:
            return True
        if node in graph:
            for child in graph[node]:
                if child not in seen:
                    seen[child] = child
                    q.append(child)
    return False


class Test(unittest.TestCase):

    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["B", "C"],
        "E": ["C", "F"],
        "F": ["E", "O", "I", "G"],
        "G": ["F", "H"],
        "H": ["G"],
        "I": ["F", "J"],
        "O": ["F"],
        "J": ["K", "L", "I"],
        "K": ["J"],
        "L": ["J"],
        "P": ["Q", "R"],
        "Q": ["P", "R"],
        "R": ["P", "Q"],
    }

    tests = [
        ("A", "L", True),
        ("A", "B", True),
        ("H", "K", True),
        ("L", "D", True),
        ("P", "Q", True),
        ("Q", "P", True),
        ("Q", "G", False),
        ("R", "A", False),
        ("P", "B", False),
    ]


    def test_is_route_bfs(self):
        for [start, end, expected] in self.tests:
            actual = is_route_bfs(self.graph, start, end)
            assert actual == expected

    def test_is_route(self):
        for [start, end, expected] in self.tests:
            actual = is_route(self.graph, start, end)
            assert actual == expected


if __name__ == "__main__":
    unittest.main()
    
