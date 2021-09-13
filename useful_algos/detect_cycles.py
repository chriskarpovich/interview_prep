# Detect cycles in graph

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS solution, detect cycles in a graph
        # adjacency list (for dependencies)
        graph = [[] for _ in range(numCourses)]
        # list for determining if we have visited a node
        visited = [False for _ in range(numCourses)]
        # DFS but when you are done with a node (i.e. done searching all of its neighbors) you mark the node as "Done" being visited
        for courses in prerequisites:
            graph[courses[0]].append(courses[1])
            
        
        def DFS(node, graph, visited):
            # base cases
            # if we are done with this node, we don't need to search it again
            if visited[node] == 1:
                return True
            # if this node has already been visited in this iteration, 
            # we have a cyclic graph, return False 
            if visited[node] == -1:
                return False
            # mark curr node as visited for this cycle and then visit all neighbors
            visited[node] = -1
            for neighbor in graph[node]:
                # if returns False, it means we have a cyclic graph
                if not DFS(neighbor, graph, visited):
                    return False
            # mark curr node as being "done" and return True, no cycles detected
            visited[node] = 1
            return True
        
        # iterate through all nodes and detect cycles
        for node in range(numCourses):
            if not DFS(node, graph, visited):
                return False
            
        return True