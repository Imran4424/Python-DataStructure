from collections import deque

class Graph:
    def __init__(self):
        self.adjList = {}

    def addEdge(self, u, v):
        if u not in self.adjList:
            self.adjList[u] = []
        if v not in self.adjList:
            self.adjList[v] = []
        self.adjList[u].append(v)
        self.adjList[v].append(u)  # Add edge in both directions for undirected graph

    def bfsPathFinding(self, startNode, endNode):
        # Initialize a queue for BFS
        queue = deque()

        # Enqueue the start node and mark it as visited
        queue.append((startNode, [startNode]))
        visited = set([startNode])

        # Perform BFS
        while queue:
            current_node, path = queue.popleft()
            # If the current node is the end node, return the path
            if current_node == endNode:
                return path
            # Enqueue neighboring nodes if they haven't been visited
            if current_node in self.adjList:
                for neighbor in self.adjList[current_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
                        visited.add(neighbor)

        # If no path is found, return None
        return None

    def dfsPathFinding(self, startNode, endNode, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        # Mark the current node as visited and add it to the path
        visited.add(startNode)
        path.append(startNode)

        # If the current node is the end node, return the path
        if startNode == endNode:
            return path

        # Recursively visit neighboring nodes
        if startNode in self.adjList:
            for neighbor in self.adjList[startNode]:
                if neighbor not in visited:
                    # Recursive call to DFS
                    result = self.dfsPathFinding(neighbor, endNode, visited, path.copy())
                    if result:
                        return result

        # If no path is found, return None
        return None

# Example usage
graph = Graph()
graph.addEdge("A", "B")
graph.addEdge("A", "C")
graph.addEdge("B", "D")
graph.addEdge("B", "E")
graph.addEdge("C", "F")
graph.addEdge("E", "F")

startNode = "A"
endNode = "F"

# BFS
pathBFS = graph.bfsPathFinding(startNode, endNode)

if pathBFS:
    print(f"Using BFS traversal, path from {startNode} to {endNode}: {' -> '.join(pathBFS)}")
else:
    print(f"No path found from {startNode} to {endNode} using BFS traversal")

# DFS
pathDFS = graph.dfsPathFinding(startNode, endNode)

if pathDFS:
    print(f"DFS Path from {startNode} to {endNode}: {' -> '.join(pathDFS)}")
else:
    print(f"No DFS path found from {startNode} to {endNode}")
