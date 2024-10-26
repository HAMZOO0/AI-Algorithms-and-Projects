# Define the Maximizer function
def maximizer(node, depth):
#     base condition
	if depth == 0 :
		return scores[node]

	best_score = -float('inf')  # Initialize with a very low score
	 
	for child in tree[node]:

		best_score = max(best_score, maximizer(child, depth - 1))

	return best_score
# Tree structure
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

# Scores at each leaf node
scores = {
    'D': 0,
    'E': -1,


    'F': 1,
    'G': -1,
    'H': 0,
    'I': 0
}


# Run the maximizer function from the root node ('A')
best_score = maximizer('A', depth=2)
print("Best score for the maximizer:", best_score)
