class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

def merge(head_a,head_b):
    
    ans = Node(0)
    temp = ans
    while head_a != None and head_b != None:
        if(head_a.data < head_b.data):
            ans.bottom = head_a
            head_a = head_a.bottom
        else:
            ans.bottom = head_b
            head_b = head_b.bottom
        ans = ans.bottom
    
    if head_a != None:
        ans.bottom = head_a
    else:
        ans.bottom = head_b
    return temp.bottom

def flatten(root):
    if(root == None):
        return None
    if(root.next == None):
        return root
    if(root.next.next == None):
        return merge(root,root.next)
    ans = merge(root,root.next)
    temp = root.next.next
    while(temp != None):
        ans = merge(ans,temp)
        temp = temp.next
    return ans
