# Explanation

The Active Directory Problem

1. Basic Data structure/concept used
    - Not a data structure but the beautiful concept of recursion
    - Though stack is the data structure used for the internal implementation of the stack(stack frames.)

2. First step was to identify the base case, which is simply when a group has only usera and no furthur groups, and then we succesively call recursion on all the subgroups.

3. Time complexity: O(n), for loop, we have.
4. Space complexity: O(1), only one variable
