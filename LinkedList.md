<center><h1>Linked Lists</h1></center><br>

## What is a Linked List?
A linked list is a linear data structure where each element is a separate object.<br>
Linked list elements are not stored at contiguous location; the elements are linked using pointers.

Each node of a list is made up of two items - the data and a reference to the next node. The last node has a reference to null. The entry point into a linked list is called the head of the list. It should be noted that head is not a separate node, but the reference to the first node. If the list is empty then the head is a null reference.

<img src="LinkedList.png" alt="Linked List Image">

## Types of Linked Lists

- Singly Linked List : Basic Linked list consists of a node that has 1 data and 1 pointer. The pointer points to the next node and so on. The last node points to null.

- Circular Linked List : Similar to Singly linked list but the last node points to the first one forming a circle.

- Doubly linked List : Each node has 1 data and 2 pointers. Usually, the left pointer points to last node and right pointer points to the next node. Circular Doubly Linked List also exist where the right pointer of last node points to first node and left pointer of first node points to last node.

## Linked List Operations

1) Traversal

2) Insert
  - Insert at start
  - Insert at Beginning
  - Insert After an element
  - Insert Before an element

3) Delete : (Algorithms are listed in Resources Section)
  - Delete at start
  - Delete at Beginning
  - Delete After an element
  - Delete Before an element

4) Search for element : Similar algos as that for Arrays

## Advantages of Linked Lists

1. They are a dynamic in nature which allocates the memory when required.
2. Insertion and deletion operations can be easily implemented.
3. Stacks and queues can be easily executed.
4. Linked List reduces the access time.

## Disadvantages of Linked Lists

1. The memory is wasted as pointers require extra memory for storage.
2. No element can be accessed randomly; it has to access each node sequentially.
3. Reverse Traversing is difficult in linked list.

## Applications of Linked Lists

- Linked lists are used to implement stacks, queues, graphs, etc.
- Linked lists let you insert elements at the beginning and end of the list.
- In Linked Lists we don't need to know the size in advance.

## Resources

You can find the Algorithms for each Operation and Many more types of Linked Lists Here:

- [GeeksForGeeks Linked List](https://www.geeksforgeeks.org/data-structures/linked-list/)
- [TutorialsPoint Linked List](https://www.tutorialspoint.com/data_structures_algorithms/linked_list_algorithms.htm)
- [Linked List - StudyTonight](https://www.studytonight.com/data-structures/introduction-to-linked-list)


- [Linked List HackerRank Course](https://www.youtube.com/watch?v=njTh_OwMljA)
- [Linked List Introduction CS Dojo](https://youtu.be/WwfhLC16bis)
- [Linked List - Abdul Bari(After this follow the suggested videos)](https://youtu.be/5C6JSsmbBoo)
- [Linked Lists in C](https://youtu.be/eGnlKPCkAFY)
- [Linked Lists Course - MU Syllabus](https://www.youtube.com/playlist?list=PLCbbVSS5VBbvh_L7DfZPN7XPXNJLq8vkE)
- [Linked Lists - CodeWhoop](https://www.youtube.com/playlist?list=PLZgR0futJAU3fCGJn2UvRWbkLqmEje_cd)
- [Linked Lists Introduction - CodeWithHarry](https://youtu.be/TWMCMvfEAv4)
- [Linked List in Python - CodeBasics](https://youtu.be/qp8u-frRAnU)
- [Linked Lists In C++ - BitDegree](https://www.bitdegree.org/learn/linked-list-c-plus-plus)
- [Linked Lists in Java](https://beginnersbook.com/2013/12/linkedlist-in-java-with-example/)
- [Linked  In Python - TutorialsPoint](https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm)
