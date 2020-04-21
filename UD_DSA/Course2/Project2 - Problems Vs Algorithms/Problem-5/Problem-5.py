
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children  = {}
        self.is_word = False
        pass
    
    def insert(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()
        pass
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        results = []
        for char, node in self.children.items():
            if node.is_word:
                results.append(suffix + char)
            results.extend(node.suffixes(suffix + char))
        return results
        
class Trie(object):
    """ The Trie itself containing the root node and insert/find functions """
    def __init__(self):
        """ Initialize this Trie (add a root node) """
        self.root = TrieNode()
    def insert(self, word):
        """ Add a word to the Trie """
        trieNode = self.root
        for char in word:
            if char not in trieNode.children:
                trieNode.insert(char)
            trieNode = trieNode.children[char]
        trieNode.is_word = True
        
    def find(self, prefix):

        if prefix == "":
            print("No results!")
        #This simply returns the node of the end character of the prefix, 
        #And if no such prefix is present it simply returns False.
        findNode = self.root
        for char in prefix:
            if char not in findNode.children:
                return False
            findNode = findNode.children[char]
        return findNode
            
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

#Input 1
print("Input 1: ")
prefix = "tr"
f(prefix)
print()

#Input 2
print("Input 2")
prefix = "an"
f(prefix)
print()

#Input 3
print("Input 3")
prefix = "f"
f(prefix)

#Outputs
# Input x