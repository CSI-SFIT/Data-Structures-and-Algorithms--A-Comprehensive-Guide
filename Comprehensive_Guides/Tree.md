<center><h1>Trees</h1></center><br>

## What is a Tree?

A tree is recursively defined as a set of one or more
nodes where one node is designated as the root of the
tree and all the remaining nodes can be partitioned into
non-empty sets each of which is a sub-tree of the root. This structure is different than a linked list whereas, in a linked list, items are linked in a linear order.

Various types of trees have been developed throughout the past decades, in order to suit certain applications and meet certain constraints. Some examples are binary search tree, B tree, treap, red-black tree, splay tree, AVL tree and n-ary tree.

## Terminology

- Root node: The root node R is the topmost node in the tree. If R = NULL, then it means the tree is empty.

- Sub-trees: If the root node R is not NULL, then the trees T1 ,
T2 , and T3 are called the sub-trees of R.

- Leaf: node A node that has no children is called the leaf node
or the terminal node.

- Path: A sequence of consecutive edges is called a path. For
example, in Fig. 9.1, the path from the root node A to node I
is given as: A, D, and I.

- Ancestor node: An ancestor of a node is any predecessor node on the
path from root to that node. The root node does not have any
ancestors. In the tree given in Fig. 9.1, nodes A, C, and G are the
ancestors of node K.

- Descendant node: A descendant node is any successor node on any
path from the node to a leaf node. Leaf nodes do not have any
descendants. In the tree given in Fig. 9.1, nodes C, G, J, and K are the
descendants of node A.

- Level number: Every node in the tree is assigned a level number in such
a way that the root node is at level 0, children of the root node are at
level number 1. Thus, every node is at one level higher than its parent.
So, all child nodes have a level number given by parent’s level number+ 1.

- Degree: Degree of a node is equal to the number of children
that a node has. The degree of a leaf node is zero.

- In-degree: In-degree of a node is the number of edges
arriving at that node.

- Out-degree: Out-degree of a node is the number of edges
leaving that node

## Types of Trees

1. General trees
2. Forests: A set of disjoint trees (or forests) is obtained by deleting the root and the edges connecting the root node to nodes at level 1.
3. Binary trees: Each Node has only 2 children.
4. Binary search trees: BST with ordered data
5. Expression trees
6. Tournament trees
7. AVL Tree
8. B Tree
9. Multi Way tree
10. B+ Tree
11. Digital Search Tree
12. Game Tree
13. Decision Tree

## Tree Operations

Each tree has different algorithms for each operation. Check out the resources or search the internet dor each algorithm

1. Traversal:
  - Inorder Traversal(LVR)
  - Preorder Traversal(VLR)
  - Postorder Traversal(LRV)

2. Insertion
3. Deletion

## Applications of Trees

- Store hierarchical data, like folder structure, organization structure, XML/HTML data.
- Binary Search Tree is a tree that allows fast search, insert, delete on a sorted data. It also allows finding closest item
- Heap is a tree data structure which is implemented using arrays and used to implement priority queues.
- B-Tree and B+ Tree : They are used to implement indexing in databases.
- Syntax Tree: Used in Compilers.
- K-D Tree: A space partitioning tree used to organize points in K dimensional space.
- Trie : Used to implement dictionaries with prefix lookup.
Suffix Tree : For quick pattern searching in a fixed text.
- Spanning Trees and shortest path trees are used in routers and bridges respectively in computer networks
- As a workflow for compositing digital images for visual effects.
## Resources

- [Decision Tree GeeksForGeeks](https://www.geeksforgeeks.org/decision-tree/)
- [Binary Tree GeeksForGeeks](https://www.geeksforgeeks.org/binary-tree-data-structure/)
- [AVL Tree - Wikipedia](https://en.wikipedia.org/wiki/AVL_tree)
- [Trees - TutorialsPoint](https://www.tutorialspoint.com/data_structures_algorithms/avl_tree_algorithm.htm)
- [Trees - Programiz](https://www.programiz.com/dsa/trees)
- [Trees - JavatPoint](https://www.javatpoint.com/tree)
- [Trees - TutorialRide](https://www.tutorialride.com/data-structures/trees-in-data-structure.htm)
<br><br>
- [Trees - Hackerrank](https://www.youtube.com/watch?v=oSWTXtMglKE)
- [Trees - MyCodeSchool](https://www.youtube.com/watch?v=qH6yxkw0u78)
- [Trees - Arnab Sen](https://www.youtube.com/playlist?list=PL-pUjcDnciX3Z5AEE8HHRrcfj-987Ia94)
- [Trees - Jenny Lectures](https://www.youtube.com/playlist?list=PL9LqbynX3r56pZA9Y1tx_ROnsNcshDAIJ)
- [Trees - Abdul Bari](https://www.youtube.com/watch?v=EWCgpVUZaB0)
- [Trees CodeBasics](https://www.youtube.com/watch?v=4r_XR9fUPhQ)

## Special Algorithms and Practice Problems

### Segment Tree :
- Algorithms
  - [Segment Tree - CPAlgorithms](https://cp-algorithms.com/data_structures/segment_tree.html)
  - [Segment Tree - Rachit Jain](https://youtu.be/Ic7OO3Uw6J0)
  - [Segment Tree - Tushar Roy](https://youtu.be/ZBHKZF5w4YU)
- Practice Problems
  - [Problem 1 - CodeForces](https://codeforces.com/contest/356/problem/A)
  - [Problem 2 - CodeForces](https://codeforces.com/problemset/problem/895/E)
  - [Problem 3 - SPOJ](http://www.spoj.com/problems/KQUERY/)
  - [Problem 4 - CodeForces](https://codeforces.com/problemset/problem/1234/D)
  - [Problem 5 - CodeForces](https://codeforces.com/contest/121/problem/E)
  - [Problem 6 - OnlineJudge](https://oj.uz/problem/view/COCI17_deda)


### Disjoint Set Union :
- Algorithms
  - [Disjoint Set Union - CPAlgorithms](https://cp-algorithms.com/data_structures/disjoint_set_union.html)
  - [Disjoint Set Union - GeeksForGeeks](https://www.geeksforgeeks.org/union-find/)
  - [Disjoint Set Union - Abdul Bari](https://youtu.be/wU6udHRIkcc)
  - [Disjoint Set Union - Tushar Roy](https://youtu.be/ID00PMy0-vE)
- Practice Problems
  - [Problem 1 - CodeChef](https://www.codechef.com/problems/GALACTIK)
  - [Problem 2 - CodeChef](https://www.codechef.com/problems/DISHOWN)
  - [Problem 3 - CodeForces](http://codeforces.com/problemset/problem/547/B)
  - [Problem 4 - CodeChef](https://www.codechef.com/problems/JABO)
  - [Problem 5 - CodeChef](https://www.codechef.com/problems/PARITREE)
  - [Problem 6 - CodeForces](http://codeforces.com/contest/151/problem/D)
  - [Problem 7 - CodeChef](https://www.codechef.com/problems/MAGICSTR)
  - [Problem 8 - CodeChef](https://www.codechef.com/problems/BIGOF01)
  - [Problem 9 - CodeChef](https://www.codechef.com/problems/FIRESC)


### Fenwick Tree :
- Algorithms
  - [Fenwick Tree - CPAlgorithms](https://cp-algorithms.com/data_structures/fenwick.html)
  - [Fenwick Tree - VisualGo](https://visualgo.net/en/fenwicktree)
  - [Fenwick Tree - Tushar Roy](https://youtu.be/CWDQJGaN1gY)
  - [Fenwick Tree - TakeUForward](https://youtu.be/9uaXG62Y8Uw)
- Practice Problems
  - [Problem 1 - OnlineJudge](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3238)
  - [Problem 2 - CodeForces](http://codeforces.com/contest/777/problem/E)
  - [Problem 3 - SPOJ](http://www.spoj.com/problems/CTRICK/)
  - [Problem 4 - SPOJ](http://www.spoj.com/problems/DQUERY/)
  - [Problem 5 - CodeForces](http://codeforces.com/contest/669/problem/E)
  - [Problem 6 - SPOJ](http://www.spoj.com/problems/YODANESS/)
  - [Problem 7 - SPOJ](http://www.spoj.com/problems/SUMSUM/)
  - [Problem 8 - SPOJ](http://www.spoj.com/problems/ADACABAA/)


### Sqrt Decomposition :
- Algorithms
  - [Sqrt Decomposition - CPAlgorithms](https://cp-algorithms.com/data_structures/sqrt_decomposition.html)
  - [Sqrt Decomposition - GeeksForGeeks](https://www.geeksforgeeks.org/sqrt-square-root-decomposition-technique-set-1-introduction/)
  - [Sqrt Decomposition - Gaurav Sen](https://youtu.be/gWbDocYhwDA)
  - [Sqrt Decomposition - CodeNCode](https://youtu.be/o7278rPg_9I)

- Practice Problems
  - [Problem 1 - SPOJ](http://www.spoj.com/problems/GIVEAWAY/)
  - [Problem 2 - OnlineJudge](https://uva.onlinejudge.org/-index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3141)
  - [Problem 3 - CodeForces](http://codeforces.com/contest/786/problem/C)
  - [Problem 4 - CodeForces](http://codeforces.com/contest/840/problem/D)
  - [Problem 5 - SPOJ](https://www.spoj.com/problems/DQUERY)
  - [Problem 6 - CodeForces](https://codeforces.com/problemset/problem/617/E)
