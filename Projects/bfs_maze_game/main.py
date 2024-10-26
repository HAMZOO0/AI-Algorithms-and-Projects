from collections import deque

# Function to perform BFS and find the path
def bfs(maze):
    # Get the size of the grid (rows and columns) 
    rows, cols = len(maze), len(maze[0])
    
    # Directions for moving: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Check if start or end are blocked
    if maze[0][0] == 1 or maze[rows-1][cols-1] == 1:
        return "No Path Found"
    
    # Queue to store (row, col, path)
    queue = deque([(0, 0, [(0, 0)])])  # Starting point (0,0) with an empty path
    
    # Visited set to keep track of visited nodes
    visited = set()
    visited.add((0, 0))
    
    while queue:
        row, col, path = queue.popleft()
        
        # If we reached the goal (bottom-right corner)
        if (row, col) == (rows-1, cols-1):
            return path
        
        # Explore neighbors
        for dr, dc in directions:
            r, c = row + dr, col + dc
            
            # Check if the neighbor is within bounds and is an open space (0)
            if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0 and (r, c) not in visited:
                visited.add((r, c))  # Mark it as visited
                queue.append((r, c, path + [(r, c)]))  # Add to queue with updated path
    
    # If the queue is empty and no path found
    return "No Path Found"

# Test the function with a sample maze
maze = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

# Call the bfs function to find the path
result = bfs(maze)

# Print the result (either the path or "No Path Found")
if isinstance(result, str):
    print(result)  # If no path is found
else:
    print("Path found:", result)  # If path is found, print the path


# len(maze) gives you the total number of rows.
# len(maze[0]) gives you the number of columns in the first row, assuming all rows have the same number of columns.


# The BFS algorithm chooses the best (shortest) path and puts all possible paths in the queue. However, as soon as it finds the shortest path to the goal, it stops processing the rest of the queue.
