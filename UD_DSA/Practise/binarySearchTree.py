from queue import Queue
class Node(object):

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def addNode(self,data):

        if self.root == None:
            self.root = Node(data)
        else:

            current = self.root
            while True:
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(data)
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(data)
                        break

    def inorder(self,node):
        if node == None:
            return
        else:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)

def height(root):

    if root == None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
        return 1 + max(lheight,rheight)

def levelOrderTraversal(root):

    if root == None:
        return
    q = Queue()
    q.put(root)
    print(root.data,end=" ")
    while not q.empty():
        curr = q.get()
        if curr.left:
            print(curr.left.data,end=" ")
            q.put(curr.left)
        if curr.right:
            print(curr.right.data,end=" ")
            q.put(curr.right)
    return


bst = BinarySearchTree()
bst.addNode(5)
bst.addNode(3)
bst.addNode(10)
bst.addNode(2)
bst.addNode(7)
bst.addNode(4)
bst.addNode(11)
bst.inorder(bst.root)
print()
print(height(bst.root))
print(levelOrderTraversal(bst.root))