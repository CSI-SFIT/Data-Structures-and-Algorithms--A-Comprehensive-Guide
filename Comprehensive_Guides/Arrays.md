<center><h1>Arrays</h1></center><br>

## What are Arrays?

An array is a structure of fixed-size, which can hold items of the same data type. It can be an array of integers, an array of floating-point numbers, an array of strings or even an array of arrays (such as 2-dimensional arrays). Arrays are indexed, meaning that random access is possible.

<img src="../Images/Arrays.png" alt="Arrays Image">

## Array Operations

Arrays have 5 types of operations:

- Traversal - Going through the array once
- Searching - Searching the array for a specific value
- Update - Updating the array at a given index
- Insertion - This cannot be done simply as size of arrays is immutable(can't be changed). So you need to define another array with length = len(orig_arr)+1
- Deletion - This cannot be done simply as size of arrays is immutable. So you need to define another array with length = len(orig_arr)-1

## Array Applications

- They are used to implement higher level of data structures like ArrayLists, Heaps, Hash Tables, etc.

## Array Algorithms

#### 1) Traversal Algorithm:

There is only one algorithms for traversal. You can go front to back or back to front. You set a counter to 0 and go on till it is less than len(arr). Then you access each entry for that using the pointer and do the operation and then reassign it.<br> In some languages like  Java and Python, instead of referring by indices to each, we can loop over the array using enhanced for loops and directly do traversal without a counter.

#### 2) Insertion Algorithm:

Insertion uses another array with length len(arr)+1. It copies all the elements till the one to be inserted then we insert the value to be inserted and then insert the rest of the array. Then we delete overwrite the original array with the new one.

#### 3) Deletion Algorithm:

Deletion uses another array with length len(arr)-1. We copy all the elements except the element to be deleted and then overwrite the original array with the new one.

#### 4) Searching Algorithms:

There are many Searching algorithms famous in the Coding community. The most prominent are:

- Linear Search
- Binary Search

There are many more like Jump Search, Interpolation Search, Exponential Search, etc.

## Resources

Links to Searching Algorithms:

- [GeeksForGeeks Searching Algorithms](https://www.geeksforgeeks.org/searching-algorithms/)

- [TutorialsPoint Page for Searching Algorithms](https://www.tutorialspoint.com/data_structures_algorithms/)

To learn more about Arrays visit the sites below:

- [Oracle Tutorial for Arrays in Java](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html)

- [Arrays in C - TutorialsPoint](https://www.tutorialspoint.com/cprogramming/c_arrays.htm)

- [Arrays in JavaScript - W3Schools](https://www.w3schools.com/js/js_arrays.asp)

- [Arrays Data Structure - GeeksForGeeks](https://www.geeksforgeeks.org/array-data-structure/)

Some Courses on Arrays are:

- [Arrays Course on CodeAcademy](https://www.codecademy.com/learn/introduction-to-javascript/modules/learn-javascript-arrays)

- [Search for MOOCs on Arrays](https://www.mooc-list.com/tags/arrays)

- [Java Arrays - Telusko](https://youtu.be/fuDNAKStpq0)

- [Complete Arrays Path - Abdul Bari](https://youtu.be/WlHUobpwxo8)

- [Arrays - CodeWithHarry](https://youtu.be/p5TDnxAYAZY)

- [Arrays - CS Dojo](https://youtu.be/pmN9ExDf3yQ)

- [Arrays in Processing - CodingTrain(Follow Suggested Videos for more)](https://youtu.be/NptnmWvkbTw)




- [Arrays In C++ - BitDegree](https://www.bitdegree.org/learn/c-plus-plus-vector)

- [Vectors in C++ - ReelLearning](https://youtu.be/SGyutdso6_c)

- [Java Array List With Examples - HowToDOInJava](https://howtodoinjava.com/java-arraylist/)

- [Lists In Python - W3Schools](https://www.w3schools.com/python/python_lists.asp)

## Popular Practice Problems

- [Problem 1 - CodeChef](https://www.codechef.com/LRNDSA01/problems/FLOW007)
- [Problem 2 - CodeChef](https://www.codechef.com/LRNDSA01/problems/ZCO14003)
- [Problem 3 - CodeChef](https://www.codechef.com/LRNDSA05/problems/BINXOR)
- [Problem 4 - LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [Problem 5 - LeetCode](https://leetcode.com/problems/container-with-most-water/)
