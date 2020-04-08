# Explanation

The LRU cache problem

Please note:
    - Problem_1.py : O(1) solution using Doubly Linked List.
    - Problem_1.1.py : O(n) solution using Queues.

1. Basic Data structure used
    - Doubly Linked List
    - Dictionary

2. Why i used Doubly linked list and a dictionary
    - So, initially i started with a queue implementation, but i was able to achieve the task in O(n) and not really O(1) as that was specified in the problem.

    - Doubly linked list provided an easy advantage of removal of elements in o(1) time and even addition to the LInked list was O(1)

    - Dictionary was used simply to hold the key value pairs, and to return it to the user as and when get method is called.
    
3. Time efficiency = O(1) for both the operations

4. Space Efficiency = O(n) as a Doubly Linked List and a dictionary were aintained.