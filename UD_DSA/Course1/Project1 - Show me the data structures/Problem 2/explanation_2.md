# Explanation

The File recursion Problem

1. Basic Data structure/concept used
    - Not a data structure but the beautiful concept of recursion
    - Though stack is the data structure used for the internal implementation of the stack(stack frames.)

2. As taught in the lessons, the first thing i looked for was the base case, that was simply when there are no more directories, we simply have to print the files and return.

3. Next, it was just calling recursion again and again on the subdirectories.

4. Time complexity: O(n)
5. Space complexity: O(n)

where n is the number of files inside the directory.