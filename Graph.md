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
