#This is the efficient code for the implementation of a queue
class Queue:

    def __init__(self,initial_size=10):
        self.arr = [0 for _ in range(0,initial_size)]
        self.front_index = -1
        self.next_index = 0
        self.queue_size = 0

    def enqueue(self,value):
        
        if self.queue_size == len(self.arr):
            self._handle_full_cap()
            pass
        # print(self.front_index,value)
        if(self.front_index == -1):
            self.front_index = 0
        self.arr[self.next_index] = value
        self.next_index = (self.next_index + 1)%len(self.arr)
        self.queue_size = self.queue_size + 1
    
    def dequeue(self):

        if (self.queue_size == 0):
            self.front_index = -1
            self.next_index = 0
            return None
        # print(self.arr[self.front_index],"hii")
        temp = self.arr[self.front_index]
        self.front_index = (self.front_index + 1)%len(self.arr)
        self.queue_size = self.queue_size -1

        if(self.queue_size == 0):
            self.front_index = -1
            self.next_index = 0
        return temp
    
    def print(self):
        for i in range(self.front_index,len(self.arr)):
            print(self.arr[i],end=" ")
        if(self.next_index < self.front_index):
            for i in range(0,self.next_index):
                print(self.arr[i],end=" ")
        print("\n")

    def size(self):
        return self.queue_size
    
    def is_empty(self):
        return (self.queue_size == 0)
    
    def front(self):
        if self.front_index == -1:
            return None
        else:
            return self.arr[self.front_index]

    def _handle_full_cap(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(0,len(old_arr))]

        #Now, we need to copy to the new array
        for i in range(self.front_index,len(old_arr)):
            self.arr[index] = old_arr[i]
            index = index + 1
        
        #Now, we need to go from the 0 to the top index
        for i in range(0,self.next_index):
            self.arr[index] = old_arr[i]
            index = index+1
        
        self.fron_index = 0
        self.next_index = index

# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")
q.print()
# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")
q.print()
# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")
