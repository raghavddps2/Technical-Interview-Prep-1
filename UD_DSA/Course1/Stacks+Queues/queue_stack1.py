# Here is our Stack Class

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()


#Wonderfule approach, to make a queue from 2 stacls.
'''
Approach:

1. Keep appending as we receive elements to an array.
2. As sson as we receive a request to dequeue an array, shift all current elements to outArray
3. Now, remove from the top, and keep on receing new elements in the InArray
4. return the size of the in and the out array if the size is asked.
'''

class Queue:
    def __init__(self):
        # Code here
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.num_elements = 0

    def size(self):
         # Code here
         return self.stack1.size()+self.stack2.size()
        
    def enqueue(self,item):
        # Code here
        self.stack1.push(item)
    def dequeue(self):
        # Code here
        if self.stack2.size() == 0:
            while self.stack1.size() != 0:
                self.stack2.push(self.stack1.pop())
        if(self.stack2.size() == 0):
            return None
        else:
            return self.stack2.pop()

# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")