class stack:

    def __init__(self):
        self.items = []

    def push(self,element):
        self.items.append(element)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
    
    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return None
    
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def size(self):
        return len(self.items)
    

    