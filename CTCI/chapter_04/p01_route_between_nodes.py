"""
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""
from graph import *
from collections import deque
import unittest

def is_route_bfs_node(node1, node2):
    # implement BFS to find path between two nodes
    def search(root, node2):
        queue = deque()
        # mark root node as seen
        root.marked = True
        # append root node to end of queue
        queue.append(root)

        while len(queue) != 0:
            # remove from front of queue
            node = queue.popleft()
            # visit node (i.e. check if node is the node we're looking for)
            if node2.value == node.value:
                # we have found the node return true
                return True
            # for each child, check if it has been seen. if not, add it to the end of the queue
            for child in node.children:
                if not child.marked:
                    # mark child as seen and append to queue
                    child.marked = True
                    queue.append(child)
        return False
    
    return search(node1, node2)

def is_route_bfs(graph, start, end):
    def search(graph, start, end):
        if start == end:
            return True
        seen = set()
        queue = deque()
        # mark root node as seen and add to queue
        seen.add(start)
        queue.append(start)

        while len(queue) != 0:
            # pop node from top of queue and visit it
            node = queue.popleft()
            if node == end:
                return True
            # mark all of node's children as seen and add to queue if they are not already seen
            for child in graph[node]:
                if child not in seen:
                    seen.add(child)
                    queue.append(child)
        return False
    return search(graph, start, end)

def is_route(graph, start, end, visited=None):
    # explore every route fully to the end (DFS)
    if visited is None:
        visited = set()
    for node in graph[start]:
        if node not in visited:
            visited.add(node)
            # recursively look to nth node
            if node == end or is_route(graph, node, end, visited):
                return True
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

    # def test_is_route(self):
    #     for [start, end, expected] in self.tests:
    #         actual = is_route(self.graph, start, end)
    #         assert actual == expected

    def test_is_route_bfs(self):
        for [start, end, expected] in self.tests:
            actual = is_route_bfs(self.graph, start, end)
            assert actual == expected

    def test_is_route(self):
        for [start, end, expected] in self.tests:
            actual = is_route(self.graph, start, end)
            assert actual == expected

    # def test_is_route_bfs_node(self):
    #     for [start, end, expected] in self.tests:
    #         nodes = []
    #         for key in self.graph:
    #             nodes.append(Node(value=key))

    #         for i in range(len(nodes)):
    #             for j in range(len(nodes)):
    #                 if nodes[j].value in self.graph[nodes[i].value]:
    #                     nodes[i].children.append(nodes[j])
    #         # for node in nodes:
    #         #     print(node.value, [x.value for x in node.children])
    #         #actual = is_route_bfs(self.graph, start, end)
    #         node1, node2 = None, None
    #         for node in nodes:
    #             if node.value == start:
    #                 node1 = node
    #             if node.value == end:
    #                 node2 = node
            
    #         actual = is_route_bfs(node1, node2)
    #         print(actual, expected)
    #         assert actual == expected


if __name__ == "__main__":
    unittest.main()
    
