--> Currently implemented Data Structures:
Hash Table(Using Open Addressing)
Binary Heap(Used in Dijkstra)

--> Currently implemented Algorithms:
Open Addressing(Double Hashing as a hash function): for Hash Table
Depth-First-Search: Used in method                AdjacencyList.isCycleExist() method
Breath-First-Search: Used in a method             __ShortestPath__.shortestPathWeighted() method
Topological Sort
Dijkstra Algorithm: Using HashTable in method:    __ShortestPath__.dijkstraV1()
Dijkstra Algorithm: Using Binary Heap in method:  __ShortestPath__.dijkstraV2()
Bellman-Ford in method:                           __ShortestPath__.bellman_ford()

GraphUsingHashTable.py takes a csv file that contain the Graphs and with their nodes and edges respectively.
But it's not necessary you can create your own graph explicitly.
GraphUsingHashTable.py works well with directed and undirected.
There is one flag isUndirected if it's True(by default it is True). Then Graph is treated as Undirected, Directed Otherwise.
Example of creating a Graph is in GraphUsingHashTable.py

There are some rules for csv file:
1. First line is used to lable if you want. I just put '#' in it.
2. Just below the '#' cell, Specify ‘,’ (comma) separated vertices. 
3. Below that cell there is bunch of pair or cells that represents edges.
4. '!' is use as End Of File.

There is a Folder 'DataSet' there are sample csv files.
Load that csv file (or csv file created by you) by load() function.
