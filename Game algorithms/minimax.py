class Node :
    def __init__(self, value=None) :
        self.value = value
        self.children = []

def minimax(node, isMax) :  
    
    if node.children == [] :
        return node.value

    if isMax : 
        best_score = -float('inf')
        
        for children in node.children :
            best_score = max(best_score , minimax(children , False))
        
        return best_score 

    else:
        best_score = +float('inf')

        for children in node.children :
            best_score = min(best_score , minimax(children , True))
        
        return best_score 


leaf1 = Node(1)
leaf2 = Node( 3)

leaf3 = Node(-5)
leaf4 = Node(0)

blk_node1 = Node()
blk_node1.children = [leaf1,leaf2]

blk_node2 = Node()
blk_node2.children = [leaf3 , leaf4]


root = Node()
root.children = [blk_node1,blk_node2]

score = minimax(root , True)
print("score --> " , score)
