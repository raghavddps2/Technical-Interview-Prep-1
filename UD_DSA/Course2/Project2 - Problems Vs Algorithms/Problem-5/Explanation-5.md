# `Autocomplete Feature using Tries`

1. Whenever, we get a new prefix, the first step if to find, the node for the last character of the prefix, because this is from where, the autocomplete suggestions should begin. So, that is achieved by the find function.

2. Now, when we find the node for the last character in prefix, we then iterate over all the children of the node we got, and then we recursively find the suffixes for suffix+char and so on.. we keep on adding to our list

3. Data Structure: Tries
4. Time complexity: O(k*c), where c is basically the number of keys in the dictionary and k is the lowest depth we go to.
 
5. Space complexity: O(n*m), n is the number of words stored in the trie and m, the longest word length