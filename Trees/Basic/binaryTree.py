#Creating the Queue class
class Queue(object):

    def __init__(self):
        self.items = []

    #Enqueuing an element to the list, we append the newly added element to the end of the list.
    def enqueue(self,item):
        self.items.insert(len(self.items),item)

    #This is simply removing the first element from the queue
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    #This just checks if the Queue is empty or not
    def is_empty(self):
        return len(self.items) == 0

    #This just returns the first element that will be removed now
    def peek(self):
        if not self.is_empty():
            return self.items[0].value

    #We override the len() method for a queue.
    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)


class Stack(object):

    #This is just defining the constructor for the stac class, we wiill just modify the list
    def __init__(self):
        self.items = []

    #We will just push the item at the end of the list
    def push(self,item):
        self.items.append(item)
    
    #We will remove the last entered element into the list
    def pop(self):

        if not self.is_empty():
            #The pop functon automatically removes the last element in the list
            return self.items.pop().value

    #This tells if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    #This gives the top element in the list
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    #This overrides the len method available and calls the size() method to get the size.
    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


#Creating the nodes
class Node(object):

    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

#Creating the binary trees
class BinaryTree(object):

    #This just simply creates the root of the tree here using the constructor
    def __init__(self,root):
        self.root = Node(root)

    #We just access the root here usiing self.
    def preOrder(self,start):

        if start == None:
            return
    
        print(start.value,end=" ")
        self.preOrder(start.left)
        self.preOrder(start.right)

    def inOrder(self,start):

        if start == None:
            return

        self.inOrder(start.left)
        print(start.value,end=" ")
        self.inOrder(start.right)

    def postOrder(self,start):

        if start == None:
            return
        
        self.postOrder(start.left)
        self.postOrder(start.right)
        print(start.value,end=" ")


    #This function will help us to perform the level order traversal, what we basically need to do 
    #here is use a queue to store the elements and then print out the left and right childs for the same.
    def levelOrder(self,start):

        if start == None:
            return 

        Q = Queue()
        Q.enqueue(start)

        while len(Q) > 0:

            #We print the node at the front
            print(Q.peek(),end=" ")

            #We dequeue the node processed
            node = Q.dequeue()
            
            #If left node exists, we enqueue it
            if node.left:
                Q.enqueue(node.left)
            
            #If right node exists, we enqueue it
            if node.right:
                Q.enqueue(node.right)

    #This is how we do the reverse order traversal from the bottom
    def reverseLevelOrder(self,start):

        Q = Queue()
        S = Stack()

        Q.enqueue(start)
        while len(Q) > 0:

            node = Q.dequeue()
            S.push(node)
            if node.right:
                Q.enqueue(node.right)
            if node.left:
                Q.enqueue(node.left)

        while len(S) > 0:
            print(S.pop(),end=" ")

    def height(self,start):
        
        #If no node, the height of the tree is not even 0, it is -1
        if start is None:
            return -1

        #This tells the left height of the tree
        left_height = self.height(start.left)
        #This tellls the right height of the tree
        right_height = self.height(start.right)

        #This returns the proper height maximum one everytime
        return 1+max(left_height,right_height)

        """
            1
           / \
        2       3
       / \     /  \
    4     5    6   7
        """

    def size1(self,start):

        if start is None:
            return 0
        return 1 + self.size1(start.left) + self.size1(start.right)

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

#Tree traversals

# E-L-R
print("PreOrder Traversal:\t")
print(tree.preOrder(tree.root))
print()

#L-E-R
print("InOrder Traversal:\t")
print(tree.inOrder(tree.root))
print()

#L-R-E
print("PostOrder Traversal:\t")
print(tree.postOrder(tree.root))
print()

#This just goes line by line
print("Level Order Traversal:\t")
print(tree.levelOrder(tree.root))
print()

#This goes line by line but from the bottom
print("Reverse Level Order Traversal:\t")
print(tree.reverseLevelOrder(tree.root))
print()

#Height of the tree
print("Height of the tree is ",tree.height(tree.root))

#SIze of the tree
print("Size of the tree is :",tree.size1(tree.root))