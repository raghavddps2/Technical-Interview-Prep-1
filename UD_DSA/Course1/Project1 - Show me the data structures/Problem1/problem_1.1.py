"THis is the O(N) solution using queues."
class Node(object):
    def __init__(self, key, x):
        self.key = key
        self.value = x
        self.next = None
        self.prev = None
    
class LRU_Cache(object):
    def __init__(self, capacity):

        self.capacity = capacity    
        self.dic = {}
        self.head = None
        self.tail = None

    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self.makeMostRecent(node)
            return node.value
        else:
            return -1

    def set(self, key, value):
        if key not in self.dic:
            if len(self.dic) == self.capacity:
                del self.dic[self.head.key]
                self.removeHead()
            node = Node(key, value)
            self.dic[key] = node
        else:
            node = self.dic[key]
            node.value = value
        self.makeMostRecent(node)
            
    def makeMostRecent(self, node):
        if self.head and self.head.key == node.key:
            self.removeHead()
        if self.tail and not self.tail.key == node.key:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            node.next = None
            self.tail.next = node  
            node.prev = self.tail  
        self.tail = node 
        if not self.head:
            self.head = node  
    
    def removeHead(self):
        self.head = self.head.next
        if self.head:
            self.head.prev = None


print("Test case 1")
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))       
print(our_cache.get(2))       
print(our_cache.get(9))      
our_cache.set(5, 5) 
our_cache.set(6, 6)
print(our_cache.get(3))      


print("Test case 2")
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)

print(our_cache.get(1))       
print(our_cache.get(2))      
our_cache.set(5, 5) 
our_cache.set(6, 6)
print(our_cache.get(3))
print(our_cache.get(5))      

print("Test case 3")
our_cache = LRU_Cache(4)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3,3) 
our_cache.set(3,6)
our_cache.set(4,4) 
our_cache.set(5,6)
print(our_cache.get(1))       
print(our_cache.get(2))      
print(our_cache.get(3))
print(our_cache.get(5))      



'''
    #Outputs for Test cases.

        Test case 1
        
        1
        2
        -1
        -1
        
        Test case 2
        
        1
        2
        -1
        5
        
        Test case 3
        
        -1
        2
        6
        6
'''