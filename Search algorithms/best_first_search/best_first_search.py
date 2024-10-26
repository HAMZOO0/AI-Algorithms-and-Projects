import heapq

# Define the graph using an adjacency list. Each node has a list of (neighbor, cost) pairs
graph = {
    'C': [('B', 14), ('T', 5), ('O', 7), ('E', 12), ('P', 15)],
    'B': [('A', 17), ('R', 20), ('S', 50)],
    'T': [],
    'O': [('I', 4), ('N', 44)],
    'E': [('G', 51)],
    'P': [('L', 0), ('F', 8), ('D', 10)],
    'I': [('Z', 0)],
    'N': [],
    'G': [],
    'L': [],
    'F': [],
    'D': [],
    'A': [],
    'R': [],
    'S': [],
    'Z': []  # Goal node
}

# Heuristic values for each node (you can modify these values based on the problem)
heuristic = {
    'C': 21, 'B': 14, 'T': 5, 'O': 7, 'E': 12, 'P': 15,
    'I': 4, 'N': 44, 'G': 51, 'L': 0, 'F': 8, 'D': 10,
    'A': 17, 'R': 20, 'S': 50, 'Z': 0
}

# Best-First Search function
def best_first_search(graph, start, goal):
    # Priority queue to explore the nodes based on the heuristic value
    priority_queue = []
    # Add the start node to the priority queue with its heuristic value and the initial path
    heapq.heappush(priority_queue, (heuristic[start], start, [start]))  # (heuristic, node, path)
    
    visited = set()  # To keep track of visited nodes
    
    while priority_queue:
        # Pop the node with the smallest heuristic value
        current_heuristic, current_node, path = heapq.heappop(priority_queue)
        
        # If we've reached the goal, return the path
        if current_node == goal:
            print(f"Goal reached! Best path: {' -> '.join(path)}")
            return path
        
        visited.add(current_node)
        
        # Explore the neighbors of the current node
        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                # Push the neighbor into the queue with its heuristic value and updated path
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor]))

# Example usage
start_node = 'C'
goal_node = 'Z'
best_first_search(graph, start_node, goal_node)
