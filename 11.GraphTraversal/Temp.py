
from collections import deque

class GraphII:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Add edge in both directions for undirected graph

    # bfs for finding path from given node to all node
    def bfsAllPath(self, startNode):
        # Initialize a queue for BFS
        queue = deque()

        # Enqueue the start node and mark it as visited
        queue.append(startNode)
        visited = {startNode: None}  # Keep track of visited nodes and their parent

        # Perform BFS to find shortest path to all nodes
        while queue:
            currentNode = queue.popleft()
            # Enqueue neighboring nodes if they haven't been visited
            if currentNode in self.graph:
                for neighbor in self.graph[currentNode]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited[neighbor] = currentNode  # Mark neighbor as visited with current node as parent

        return visited
    
    # dfs for finding path from given node to all node
    def dfsAllPath(self, startNode):
        # Initialize a stack for DFS
        stack = [(startNode, [startNode])]
        visited = set()

        # Perform DFS to find paths to all nodes
        dfsAllPath = {}
        while stack:
            currentNode, path = stack.pop()
            if currentNode not in visited:
                visited.add(currentNode)
                dfsAllPath[currentNode] = path
                for neighbor in self.graph.get(currentNode, []):
                    stack.append((neighbor, path + [neighbor]))
        return dfsAllPath

# Example usage
graph = GraphII()
graph.addEdge("A", "B")
graph.addEdge("A", "C")
graph.addEdge("B", "D")
graph.addEdge("B", "E")
graph.addEdge("C", "F")
graph.addEdge("E", "F")

startNode = "A"

# BFS shortest path from start node to all other nodes
bfsAllPath = graph.bfsAllPath(startNode)
for node, parent in bfsAllPath.items():
    path = [node]
    while parent:
        path.append(parent)
        parent = bfsAllPath[parent]
    path.reverse()
    print(f"Shortest path from {startNode} to {node}: {' -> '.join(path)}")
    

print("")
print("")

# DFS paths from start node to all other nodes
dfsAllPath = graph.dfsAllPath(startNode)
for node, path in dfsAllPath.items():
    print(f"Path from {startNode} to {node}: {' -> '.join(path)}")
