class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

def merge(root1,root2):
    ans = Node(0)
    ref1 = root1
    ref2 = root2

    while(ref1 != None or ref2 != None):
        if(ref1.data < ref2.data):
            ans.next = ref1
            ref1 = ref1.next
        else:
            ans.next = ref2
            ref2 = ref2.next
        ans = ans.next
    
    return ans.next