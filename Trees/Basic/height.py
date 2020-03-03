class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


#This is how i will calculate the height of a tree iteratively!
def height(root):

    #If the root itself is null, the height of the tree is straight away 0.
    if root == None:
        return 0

    #We design a queue, where we keep all the elements at the current level!
    q = []
    q.append(root)
    height = 0
    while(True):

        n = len(q)

        #If no elements, all we have to do is return the current height
        if n == 0:
            return height
        
        #else we add one for each level.
        height = height + 1 

        #We deal with all the elements in the array at the current level and pop all of them out
        #and we include the new elements!
        while n > 0:
            node = q[0]
            q.pop(0)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
            n = n-1
        
if __name__ == "__main__":
    
    root = Node(1)
    root.left = Node(2)
    root.left = Node(3)
    root.left.left = Node(4)
    print(height(root))
