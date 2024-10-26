# C++ code for Adjacency list
```

#include <iostream>
#include <list>
#include <map>
using namespace std;

class Graph
{

    map<int, list<int>> adjList;

public:
    void addEdge(int u, int v, bool bidir = true)
    {
        adjList[u].push_back(v);
        if (bidir)
        {
            adjList[v].push_back(u);
        }
    }

    void print()
    {
        for (auto i : adjList)
        {

            cout << i.first << "->";
            for (auto j : i.second)
            {
                cout << j << " ";
            }
            cout << endl;
        }
    }
};
int main(int argc, char const *argv[])
{
    Graph g;
    g.addEdge(0, 1);
    g.addEdge(0, 4);
    g.addEdge(1, 2);
    g.addEdge(2, 3);
    g.addEdge(3, 4);
    g.addEdge(4, 5);
    g.print();
    return 0;
}
```
