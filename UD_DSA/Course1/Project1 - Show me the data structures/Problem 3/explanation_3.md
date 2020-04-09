## Huffman Coding

Basically the Huffman algorithm is used for data compression.

A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored in the leaves.

The time complexity of the Huffman algorithm is `O(nlogn)`. By using a heap to store the weight of each tree, each iteration requires `O(log n)` time to place in the priority queue, and there are `O(n)` iterations, one for each item. The space complexity in building the Huffman Tree is `O(#of distinct symbols in the data)`. 
