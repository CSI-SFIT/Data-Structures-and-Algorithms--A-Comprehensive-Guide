<center><h1>Queues</h1></center><br>

## What is a Queue?

A Queue is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first. The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.

<img src="Queue.png" alt="Queues Image" />

## Queue Implementations

- Array representation : Queues have 2 pointers. FRONT and REAR. Initially both are null. When an element is added both are 0. Enqueuing is done from the REAR. It is incremented when another element is added.

- Linked list representation : In Linked List, 2 pointers FRONT and REAR are there which point to them.

## Queue Operations

1. Enqueue(Inserion) : In Array representation, REAR is incremented and at READ the variable is assigned.
<br>In Linked List, a new node is created with the value and the REAR element's pointer is assigned to new node and REAR is pointed to new node.
2. Dequeue(Deletion) : In Array representation, Front is incremented.
<br>In Linked List, the FRONT node is freed/deleted, FRONT is pointed to the next node of the original FRONT node.

## Types of Queues

- Linear Queue: Basic queue with FRONT and REAR as previously told
- Circular Queue: For linked list, Circular Linked List is used. For Array, as soon as FRONT or REAR exceed MAX, they are assigned to 0(if front is not 0)
- Double Ended Queue(Deque - not same as Dequeue): In it enqueuing and dequeuing can be don't from both ends. There are 2 types :
  - Input Restricted Deque - Enqueuing is allowed only from rear. Dequeuing can be done from both front and rear
  - Output Restricted Deque - Dequeuing is allowed only from front. Enqueuing is allowed from both front and rear.
- Priority Queue: Each element in Priority Queue has a priority level. It is used in OS for scheduling tasks.

## Application of Queues

- Serving requests on a single shared resource, like a printer, CPU task scheduling etc.
- In real life scenario, Call Center phone systems uses Queues to hold people calling them in an order, until a service representative is free.
- Handling of interrupts in real-time systems. The interrupts are handled in the same order as they arrive i.e First come first served

## Resources

- [Queue - GeeksForGeeks](https://www.geeksforgeeks.org/queue-data-structure/)
- [Queue - TutorialsPoint](https://www.tutorialspoint.com/data_structures_algorithms/dsa_queue.htm)
- [Queue - Programiz](https://www.programiz.com/dsa/queue)
- [Queue - StudyTonight](https://www.studytonight.com/data-structures/queue-data-structure)
- [Queue - Python Docs](https://docs.python.org/3/library/queue.html)<br><br>

- [Queue Video Lecture - Jenny Lectures](https://www.youtube.com/watch?v=zp6pBNbUB2U)
- [Queue in C](https://www.youtube.com/watch?v=gnYM_G1ILm0)
- [Queue - MyCodeSchool](https://www.youtube.com/watch?v=okr-XE8yTO8)
- [Queue - Esucation4You](https://www.youtube.com/watch?v=HI34Oytjjb4)
- [Queue - Abdul Bari(Follow Suggested Videos for more)](https://www.youtube.com/watch?v=nNnGh0N9P48)
- [Queues - CodeWithHarry](https://www.youtube.com/watch?v=JlZX7xIBjl0)
- [Stacks, Queues And Priority Queues](https://drive.google.com/file/d/0B4AmxgIIrh_SUjN2VXE0NU5Benc/view)
- [Stacks And Queues - Princeton](https://introcs.cs.princeton.edu/java/43stack/)
- [Stacks And Queues In Python](https://stackabuse.com/stacks-and-queues-in-python/)
