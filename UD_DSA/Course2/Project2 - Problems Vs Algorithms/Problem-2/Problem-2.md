# `Search in a Rotated Sorted Array`

1. This was a reallyy nice problem, As we had to search and the allowed time complexity was O(log(n)), I gt an hint as to binary search should be applied here.

2. I applied binary search and retrieved the pivot, as to the point from where the array is rotated, after that, I simply checked if the in which array the target lies, and I applied binarySearch in that Direction

3. Time complexity: O(log(n))
4. Data Structures used: Arrays
5. Space Complexity: O(1), I am just passing the sliced arrays in functions, that doesn't account to space complexity.