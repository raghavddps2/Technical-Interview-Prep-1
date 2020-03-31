class Stack:


    def __init__(self):
        self.stack = []
        self.size = 0
    
    def push(self,data):
        self.stack.insert(0,data)
        self.size = self.size + 1

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def pop(self):
        if self.size == 0:
            return -1
        else:
            self.size = self.size - 1
            return self.stack.pop(0)

    def Ssize(self):
        return self.size
    
    def peak(self):
        if(self.size == 0):
            return -1
        else:
            return self.stack[0]
    
def main():

    #Creating an object of the sstack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.peak())
    print(stack.pop())
    print(stack.peak())
    print(stack.pop())
    print(stack.peak())



if __name__ == "__main__":
    main()