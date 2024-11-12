 
class Graph : 
    def __init__(self):
        self.adgList= {}
        self.visited= {}

    def addEdge(self ,u,v , check = True ):
        if u not in self.adgList :
            self.adgList[u]= []
        self.adgList[u].append(v)

        if check :
            if v not in self.adgList :
                self.adgList[v]= []
            
            self.adgList[v].append(u)

    def dfs(self , start):
        self.visited[start]= True
        print(start)

        for neighbor in self.adgList[start]:
            if neighbor not in self.visited:  # Only visit if not visited
                self.dfs(neighbor)

    
g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 6)
g.addEdge(4, 7)

print("Following is the Depth-First Search (DFS):")
g.dfs(1)  # Start DFS from node 1
