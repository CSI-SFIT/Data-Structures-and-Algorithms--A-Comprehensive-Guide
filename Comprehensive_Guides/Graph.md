<center><h1>Graphs</h1></center><br>

## What are Graphs?

A graph consists of a finite set of vertices or nodes and a set of edges connecting these vertices.
The order of a graph is the number of vertices in the graph. The size of a graph is the number of edges in the graph.
Two nodes are said to be adjacent if they are connected to each other by the same edge.

## Types Of Graphs

There area lot of types for graphs. I'm listing the top ones. Check out the resources for many many more.

1. Directed Graphs
2. Undirected Graphs
3. Tree(Tree is a graph with no cycles)
4. Bipartite Graphs
5. Complete Graphs

## Representing Graphs

1. Adjacency Matrix: It is used to represent directed graphs. It contains of a matrix with each element representing the weight of the connection between those 2 nodes

2. Adjacency List: It consists of a list where each element is the weight of path between the connection of that element and all other elements

3. Edge List: It consists of elements in format (x,y,z) where x is 1 node and y is another node and z is the weight between x and y


## Common Problems in Graphs

- Shortest Path Problem
- Continuity
- Number of Negative Cycles
- Finding Strongly Connected Components
- Travelling Salesman Problem
- Finding Bridges between 2 nodes
- Finding Articulation Points
- Finding Minimum Spanning Trees
- Finding Network Flow

## Algorithms

- DFS(Depth First Search)
- BFS(Breadth First Search)
- A* Search
- Djikstra's Algorithm, etc.

## Uses of Graphs

- In Computer science graphs are used to represent the flow of computation.
- Google maps uses graphs for building transportation systems, where intersection of two(or more) roads are considered to be a vertex and the road connecting two vertices is considered to be an edge, thus their navigation system is based on the algorithm to calculate the shortest path between two vertices.
- In Facebook, users are considered to be the vertices and if they are friends then there is an edge running between them. Facebook’s Friend suggestion algorithm uses graph theory. Facebook is an example of undirected graph.
- In World Wide Web, web pages are considered to be the vertices. There is an edge from a page u to other page v if there is a link of page v on page u. This is an example of Directed graph. It was the basic idea behind Google Page Ranking Algorithm.
- In Operating System, we come across the Resource Allocation Graph where each process and resources are considered to be vertices. Edges are drawn from resources to the allocated process, or from requesting process to the requested resource. If this leads to any formation of a cycle then a deadlock will occur.

## Resources

- [Graphs - GeeksForGeeks](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)
- [Graphs - TutorialsPoint](https://www.tutorialspoint.com/data_structures_algorithms/graph_data_structure.htm)
- [Graphs - Programiz](https://www.programiz.com/dsa/graph)
- [Graphs - HackerEarth](https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/tutorial/)
- [Graphs - Educative](https://www.educative.io/edpresso/what-is-a-graph-data-structure)
- [Graphs JavatPoint](https://www.javatpoint.com/ds-graph)


- [Graphs - MyCodeSchool](https://www.youtube.com/watch?v=gXgEDyodOJU&t=154s)
- [Graphs - Jenny's Lectures](https://www.youtube.com/watch?v=5hPfm_uqXmw)
- [Graphs - GeeksForGeeks](https://www.youtube.com/playlist?list=PLqM7alHXFySEaZgcg7uRYJFBnYMLti-nh)
- [Graphs - Abdul Bari](https://www.youtube.com/watch?v=pcKY4hjDrxk)

## Special Algorithms and Practice Problems
### BFS and DFS
- Algorithms
  - [BFS and DFS - HackerRank](https://youtu.be/zaBhtODEL0w)
  - [BFS and DFS - Abdul Bari](https://youtu.be/pcKY4hjDrxk)

- Practice Problems
  - [Problem 1 - SPOJ](http://www.spoj.com/problems/PPATH/)
  - [Problem 2 - CodeForces](https://codeforces.com/problemset/problem/910/A)
  - [Problem 3 - Codechef](https://www.codechef.com/problems/FIRESC)
  - [Problem 4 - SPOJ](http://www.spoj.com/problems/BUGLIFE/)
  - [Problem 5 - SPOJ](http://www.spoj.com/problems/KFSTB/)
  - [Problem 6 - CodeForces](https://codeforces.com/problemset/problem/500/A)
  - [Problem 7 - CodeForces](https://codeforces.com/problemset/problem/727/A)
  - [Problem 8 - SPOJ](http://www.spoj.com/problems/ELEVTRBL/)
  - [Problem 9 - SPOJ](http://www.spoj.com/problems/ROBOTGRI/)
  - [Problem 10 - CodeForces](https://codeforces.com/problemset/problem/129/B)
  - [Problem 11 - SPOJ](http://www.spoj.com/problems/LABYR1/)
  - [Problem 12 - SPOJ](http://www.spoj.com/problems/QUEEN/)


### DFS
- Algorithms
  - [DFS - CP Algorithms](https://cp-algorithms.com/graph/depth-first-search.html)
  - [DFS -
Sundeep Saradhi Kanthety](https://youtu.be/xwlRWdAHMBg)
  - [DFS - Gate Smashers](https://youtu.be/f8luGFRtshY)

### BFS
- Algorithms
  - [BFS - CP Algorithms](https://cp-algorithms.com/graph/breadth-first-search.html)
  - [BFS - Sundeep Saradhi Kanthety](https://youtu.be/cMELxr5hKYU)
  - [BFS - Gate Smashers](https://youtu.be/qul0f79gxGs)


### Kruskal's Algorithm to find Minimum Spanning Tree
- Algorithms
  - [Kruskal's Algorithm - CP Algorithms](https://cp-algorithms.com/graph/mst_kruskal.html)
  - [Kruskal's Algorithm - Abdul Bari](https://youtu.be/4ZlRH0eK-qQ)
  - [Kruskal's Algorithm - Gate Smashers](https://youtu.be/huQojf2tevI)

- Practice Problems
  - [Problem 1 - SPOJ](https://www.spoj.com/problems/MST/)
  - [Problem 2 - CodeChef](https://www.codechef.com/problems/MSTQS)
  - [Problem 3 - SPOJ](http://www.spoj.com/problems/NITTROAD/)
  - [Problem 4 - CodeChef](https://www.codechef.com/problems/GALACTIK)
  - [Problem 5 - SPOJ](http://www.spoj.com/problems/KOICOST/)
  - [Problem 6 - SPOJ](http://www.spoj.com/problems/CSTREET/)
  - [Problem 7 - SPOJ](http://www.spoj.com/problems/BLINNET/)
  - [Problem 8 - CodeChef](https://www.codechef.com/problems/GOOGOL03)
  - [Problem 9 - SPOJ](http://www.spoj.com/problems/HIGHWAYS/)
  - [Problem 10- SPOJ](http://www.spoj.com/problems/IITWPC4I/)


### Dijkstra's Algorithm(Pathfinding in Graph)
- Algorithms
  - [Dijkstra's Algorithm - CP Algorithms](https://cp-algorithms.com/graph/dijkstra.html)
  - [Dijkstra's Algorithm - GeeksForGeeks](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
  - [Dijkstra's Algorithm - Programiz](https://www.programiz.com/dsa/dijkstra-algorithm)
  - [Dijkstra's Algorithm - Abdul Bari](https://youtu.be/XB4MIexjvY0)
  - [Dijkstra's Algorithm - Computer Science](https://youtu.be/pVfj6mxhdMw)

- Practice Problems
  - [Problem 1 - CodeChef](https://www.codechef.com/problems/HW3G)
  - [Problem 2 - CodeForces](https://codeforces.com/contest/715/problem/B)
  - [Problem 3 - CodeChef](https://www.codechef.com/problems/STRGRA)
  - [Problem 4 - SPOJ](https://www.spoj.com/problems/EZDIJKST/)
  - [Problem 5 - CodeChef](https://www.codechef.com/problems/INLO33)
  - [Problem 6 - CodeForces](https://codeforces.com/contest/59/problem/E)
  - [Problem 7 - CodeChef](https://www.codechef.com/problems/KNGPRB)
  - [Problem 8 - CodeChef](https://www.codechef.com/problems/PAIRCLST)
  - [Problem 9 - CodeForces](https://codeforces.com/contest/449/problem/B)
  - [Problem 10 - CodeChef](https://www.codechef.com/problems/DIGJUMP)



### Prim's Algorithm to find Minimum Spanning Tree
- Algorithms
  - [Prim's Algorithm - CP Algorithms](https://cp-algorithms.com/graph/mst_prim.html)
  - [Prim's Algorithm - GeeksForGeeks](https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/)
  - [Prim's Algorithm - TutorialsPoint](https://www.tutorialspoint.com/data_structures_algorithms/prims_spanning_tree_algorithm.htm)
  - [Prim's Algorithm - Jenny's Lectures](https://youtu.be/ZtZaR7EcI5Y)
  - [Prim's Algorithm - GeeksForGeeksYT](https://youtu.be/eB61LXLZVqs)
