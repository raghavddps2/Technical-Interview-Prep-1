# Explanation

The Union and Intersection problem

1. Basic Data structure used
    - Linked lists
    - sets

2. The data structure used is sets and linked list,the first approach to search in list 2 and then in list2, came out to be o(m*n),though space complexity was less, so i went with the set method.

3. I used one set to store all the elements of one linked list, and for intersection i just checked if the element in second list was present in set 1, this was done in O(1) time as lookups in sets are o(1) time.

4. For union, i first entered all the elements in the set for ll1, as all will be present, then for second list, i entered the ones which are not present already in set1, this was also done in O(1) time, as sets have O(1) lookup time.

5. Time efficiency = Greater of (O(m) or O(n)) where m and n are the number of elements in the two linked lists.

6. Space Efficiency = O(m+n) for the union case and O(n) or O(m) whichever is greater.

7. Please note: In the solution, the duplicate numbers are considered only once.
    Reason: I just went through the intersection method defined on sets, and they also do intersection and union in the same way. Example shown below.
    
                            >>> a = {1,2,3,1}
                            >>> b = {1,1,1,1}
                            >>> a.intersection(b)
                            {1}
                            >>> a.union(b)
                            {1, 2, 3}
