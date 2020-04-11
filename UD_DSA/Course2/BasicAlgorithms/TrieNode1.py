class TrieNode(object):

    #Trie Node class.
    def __init__(self,char=None):

        #This represents all the nodes of the trieNode.
        self.children = [None]*26
        #isEndOfWord is true if node represents end of the word,
        self.character = char
        self.isEndOfWord = False

class Trie(object):

    def __init__(self):
        self.root = self.getNode()


    def getNode(self):
        return TrieNode()
        
    def _charToIndex(self,ch):
        return ord(ch)-ord('a')
    
    def insert(self,key):

        '''
            1. While adding a key to the trie, two cases might arise.
                i) The new key added to the trie is not a part of the trie
                ii) The new key added to the trie is already a part of the prefix node.
        '''
        builderNode = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            #If character is not already present.
            if not builderNode.children[index]:
                builderNode.children[index] = self.getNode()
            builderNode = builderNode.children[index]
        
        builderNode.isEndOfWord = True
    
    def search(self,key):

        #Our task here is to check if the key is present in the trie.
        length = len(key)
        builderNode  = self.root
        for level in range(length):
            index = self._charToIndex(key[level])
            if not builderNode.children[index]:
                return False
            builderNode  = builderNode.children[index]
        
        return builderNode.isEndOfWord

    #Helper function to tell if the rooot has no children.
    def isEmpty(self,trieNode):
        for i in trieNode.children:
            if i is not None:
                return False
        return True
    
    def remove(self,trieNode,key,depth=0):

        if(trieNode is None):
            return None
        
        if(depth == len(key)):
            if(trieNode.isEndOfWord):
                trieNode.isEmpty = False
            
            if(self.isEmpty(trieNode)):
                trieNode = None
            
            return trieNode
        
        index = ord(key[depth]) - ord('a')
        trieNode.children[index] = self.remove(trieNode.children[index],key,depth+1)

        if(self.isEmpty(trieNode) and trieNode.isEndOfWord == False):
            trieNode = None
        return trieNode
        


def main():

    trie = Trie()
    keys = ['raghav','geeks','radhika','rahul','gambling','geeky','ra']
    for key in keys:
        trie.insert(key)
    
    print("Present in trie {}".format(trie.search("raghav")))
    print("Present in trie {}".format(trie.search("rahulai")))
    print("Present in trie {}".format(trie.search("rahul")))
    print("Present in trie {}".format(trie.search("radhika")))    
    trie.remove(trie.root,"radhika")
    trie.remove(trie.root,"rahul")
    print("Present in trie {}".format(trie.search("radhika")))
    print("Present in trie {}".format(trie.search("rahul")))
if __name__ == "__main__":
    main()

