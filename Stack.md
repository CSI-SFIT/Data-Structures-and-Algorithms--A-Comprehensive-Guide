<center><h1>Stack</h1></center><br>

## What is a Stack?

Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).

There are many real-life examples of a stack. Consider an example of plates stacked over one another in the canteen. The plate which is at the top is the first one to be removed, i.e. the plate which has been placed at the bottommost position remains in the stack for the longest period of time. So, it can be simply seen to follow LIFO(Last In First Out)/FILO(First In Last Out) order.

<img src="Stack.png" alt="Stack Image">

## Stack Implementations

1.Array: There is a TOP pointer that always points to the top element. Initially it is NULL. On adding 1 element is becomes 0 and so on. It also has a MAX variable which contains the size of the array at time of declaration. If TOP is MAX-1 and we try to add another element we give OVERFLOW ERROR(can't add anymore) and if we try to delete when TOP=NULL then we give UNDERFLOW ERROR(can't delete from empty stack).

2.Linked List: There is a TOP pointer that points to top node. Initially is NULL. if TOP is NULL and we try to delete we give UNDERFLOW. There is no OVERFLOW as Linked List is dynamic and can have as many nodes as possible.

## Stack Operations

1. Push(Insertion) : If implementing Array, we initialize the TOP+1 position as the value and increment TOP. We check the conditions written in Implementation.
<br> If implementing as a Linked List, we check condition, point TOP node's pointer to new node, append value to the list and point TOP to the new node.

2. Pop(Deletion) : If implementing Array, we check the conditions and decrement TOP.<br>
If implementing as a Linked List, we check condition, point the second to last node's pointer to null, point TOP to second to last element and free/delete last node.

There are other operations too like peek, etc. but they use the same logic as Push and Pop.

## Advantages of Stack

- Helps you to manage the data in a Last In First Out(LIFO) method which is not possible with Linked list and array.
- When a function is called the local variables are stored in a stack, and it is automatically destroyed once returned.
- A stack is used when a variable is not used outside that function.
- It allows you to control how memory is allocated and deallocated.
- Stack automatically cleans up the object.
- Not easily corrupted
- Variables cannot be resized.

## Disadvantages of Stack

- Stack memory is very limited.
- Creating too many objects on the stack can increase the risk of stack overflow.
- Random access is not possible.
- Variable storage will be overwritten, which sometimes leads to undefined behavior of the function or program.
- The stack will fall outside of the memory area, which might lead to an abnormal termination.

## Application of Stack

- It is used in expression parsing, to check format in commands, etc.
- They are used in Backtracking algorithms.

## Resources

- [Stack - GeeksForGeeks](https://www.geeksforgeeks.org/stack-data-structure/)
- [Stack - Programiz](https://www.programiz.com/dsa/stack)  
- [Stack - TutorialsPoint](https://www.tutorialspoint.com/data_structures_algorithms/stack_algorithm.htm)  
- [Stack - JavaDocs](https://docs.oracle.com/javase/7/docs/api/java/util/Stack.html)  
- [Stack - StudyTonight](https://www.studytonight.com/data-structures/stack-data-structure)
<br><br>
- [Stack Video Course- GeeksForGeeks](https://www.youtube.com/playlist?list=PLqM7alHXFySF7Lap-wi5qlaD8OEBx9RMV)  
- [Stack in C](https://youtu.be/BrVZZZkkGGI)  
- [Stack - Jenny's Lectures](https://youtu.be/bxRVz8zklWM)  
- [Introduction to Stacks - Abdul Bari(Follow Suggested Videos for more)](https://youtu.be/HXE1arB8NNs)
- [Stacks - CodeWithHarry](https://youtu.be/-n2rVJE4vto)  
- [Stacks - Aditya Verma](https://www.youtube.com/playlist?list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd)
