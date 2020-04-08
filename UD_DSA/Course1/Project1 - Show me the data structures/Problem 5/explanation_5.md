# Explanation

The Blockchain problem

1. Basic Data structure used
    - Singly Linked List.

2. This was the most interesting problem, as i read about blockchain and its various usecases and various concepts like proof of concept etc.

3. I used a singly linked list, as all i had to do was to link the blocks,
    here i used a nice technique, instead of linking to the next pointer, i stored the entire block in the previous hash to retrieve it later.
4. Time efficiency = O(1) for adding to block

5. Space Efficiency = O(n) as a there might be n blocks.