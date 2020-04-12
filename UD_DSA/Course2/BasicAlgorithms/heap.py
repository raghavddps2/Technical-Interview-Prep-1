class Heap:

    def __init__(self,initial_size):
        self.cbt = [None for _ in range(0,initial_size)]
        self.next_index = 0

    def up_heapify(self):
        child_index = self.next_index
        while child_index >= 1:
            parent_index = (child_index-1)//2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element
                child_index = parent_index
            else:
                break
    
    def down_heapify(self):
        parent_index = 0
        while parent_index < self.next_index:
            left_index = 2*parent_index + 1
            right_index = 2*parent_index + 2
            parent_element = self.cbt[parent_index]
            left_child = None
            right_child = None

            min_element = parent_element
            if left_index < self.next_index:
                left_child = self.cbt[left_index]
            if right_index < self.next_index:
                right_child  = self.cbt[right_index]
            
            if left_child is not None:
                min_element = min(parent_element,left_child)
            if right_child is not None:
                min_element = min(right_child,min_element)

            if min_element == parent_element:
                return
            
            if min_element == left_child:
                self.cbt[left_index] = parent_element
                self.cbt[parent_index] = min_element
                parent_index = left_index
            elif min_element == right_child:
                self.cbt[right_index] = parent_element
                self.cbt[parent_index] = min_element
                parent_index = right_index            

    def insert(self,data):

        self.cbt[self.next_index] = data
        self.up_heapify()
        self.next_index += 1

    def size(self):
        return self.next_index

    def remove(self):
        if self.size() == 0:
            return None
        self.next_index = self.next_index - 1
        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]
        self.cbt[0] = last_element
        self.cbt[self.next_index] = to_remove
        self.down_heapify()
        return to_remove

    def print(self):
        for i in range(0,self.next_index):
            print(self.cbt[i])


heap = Heap(10)
heap.insert(10)
heap.insert(20)
heap.insert(30)
heap.insert(40)
heap.insert(50)
heap.insert(15)
heap.remove()
heap.print()

