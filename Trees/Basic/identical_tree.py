class Node:

    def __init__(self,data):

        self.data = data
        self.left = None
        self.right = None


"""
    This is the important function we need to talk about.

    not node1 and not node2 implies
        the tree no longer exixts or we have reached the end of the tree
"""

def isIdentical(node1,node2):

    if not node1 and not node2:
        # print("Ho")
        return True
    
    if node1 and node2 and node1.data == node2.data:

        a = isIdentical(node1.left,node2.left) 
        print("Hi")
        b =  isIdentical(node1.right,node2.right)
        print("Hello")
        return a and b
    else:
        return False

if __name__ == '__main__':

    root1 = Node(1)
    root2 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)

    root2.left = Node(2)
    root2.right = Node(3)

    print(isIdentical(root1,root2))