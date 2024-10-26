 import heapq c

# Predefined graph (edges with costs)
graph = {
   'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3}, 
    'D': {'B': 2, 'E': 1},
    'E': {'B': 5, 'D': 1, 'G': 2},
    'F': {'C': 3, 'G': 2},
    'G': {'E': 2, 'F': 2}
}

# Heuristic function (estimated cost to goal)
heuristic = {
        'A': 7, 'B': 6, 'C': 4, 'D': 5, 'E': 3, 'F': 2, 'G': 0

}

def a_star(graph, start, goal):
    open_list = []  # List of nodes to explore
    heapq.heappush(open_list, (0, start))  # Add start node with cost 0
    came_from = {}  # Tracks path
    g_cost = {start: 0}  # Cost from start to each node
    
    while open_list:
        current_cost, current_node = heapq.heappop(open_list)  # Node with lowest cost
        
        if current_node == goal:
            return reconstruct_path(came_from, start, goal)
        
        for neighbor, cost in graph[current_node].items():
            new_cost = g_cost[current_node] + cost
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                total_cost = new_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)
                heapq.heappush(open_list, (total_cost, neighbor))
                came_from[neighbor] = current_node

    return None  # If goal is not reached

# Function to reconstruct the path from start to goal
def reconstruct_path(came_from, start, goal):
    path = [goal]
    while goal != start:
        goal = came_from[goal]
        path.append(goal)
    path.reverse()  # Reversed path (from goal to start)
    return path

# Running the algorithm
start_node = 'A'
goal_node = 'G'
path = a_star(graph, start_node, goal_node)
print("Shortest path:", path)
