# BFS algorithm
from collections import deque
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
        
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"
        
def bfs(tree):
    
    q = Queue()
    q.enq(tree.get_root())
    visited_answer = []
    while(len(q) > 0):
        node = q.deq()
        visited_answer.append(node.value)
        if node.left:
            q.enq(node.left)
        if node.right:
            q.enq(node.right)
    return visited_answer
    pass