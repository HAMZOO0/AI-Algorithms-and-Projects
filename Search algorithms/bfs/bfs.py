from collections import deque

class Graph:

    def __init__(self):
        # Using a dictionary to store the adjacency list -> key-value pair 
        self.adjList = {}
    def addEdge(self, u, v, bidir=True):
        # If 'u' is not in adjList, initialize with an empty list
        if u not in self.adjList:
            self.adjList[u] = []
        # Add the edge from 'u' to 'v'
        self.adjList[u].append(v)

        if bidir:
            # If 'v' is not in adjList, initialize with an empty list
            if v not in self.adjList:
                self.adjList[v] = []
            # Add the edge from 'v' to 'u' for bidirectional graphs
            self.adjList[v].append(u)

    def print(self):
        # Printing the adjacency list
        for node in self.adjList:
            print(f"{node}: {self.adjList[node]}")
            
    def bfs(self , start):
         # Dictionary to keep track of visited nodes
         visited = {}

         visited[start] = True 
         queue = deque([start])

         while queue:

             node = queue.popleft()

             print(node)

             for neighbour in self.adjList[node]:
                 if neighbour not in visited:
                    visited[neighbour] = True  # Mark as visited
                    queue.append(neighbour)

# Creating the graph object and adding edges
G1 = Graph()
G1.addEdge(0, 1)
G1.addEdge(0, 2)
G1.addEdge(1, 2)
G1.addEdge(2, 0)
G1.addEdge(2, 3)
G1.addEdge(3, 3)

# Print the adjacency list of the graph
# G1.print()
G1.bfs(0)
