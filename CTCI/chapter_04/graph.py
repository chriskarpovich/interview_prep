class Node():
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.marked = False


class Graph():
    def __init__(self, nodes=None):
        self.nodes = []
        if nodes:
            self.nodes = nodes
        

    
