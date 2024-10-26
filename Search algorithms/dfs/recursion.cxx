#include <iostream>
#include <list>
#include <map>
#include <stack>
using namespace std;

class Graph
{
    map<int, list<int>> adjList; // Adjacency list representation of the graph
    map<int, bool> visited;      // Map to keep track of visited nodes

public:
    // Function to add an edge to the graph
    void addEdge(int u, int v)
    {
        adjList[u].push_back(v); // Add v to the adjacency list of u
    }

    // Recursive DFS function
    void dfsRecursive(int node)
    {
        visited[node] = true; // Mark the current node as visited
        cout << node << " ";  // Print the current node

        // Explore all adjacent nodes
        for (int neighbor : adjList[node])
        {
            if (!visited[neighbor])
            {                           // If the neighbor hasn't been visited
                dfsRecursive(neighbor); // Recur for the neighbor
            }
        }
    }

    // Function to initiate DFS
};

// Driver Code
int main()
{
    Graph g;
    g.addEdge(1, 2);
    g.addEdge(1, 3);
    g.addEdge(2, 4);
    g.addEdge(2, 5);
    g.addEdge(3, 6);
    g.addEdge(4, 7);

    cout << "Following is the Depth-First Search:\n";
    g.dfsRecursive(1); // Start DFS from node 1

    return 0;
}
