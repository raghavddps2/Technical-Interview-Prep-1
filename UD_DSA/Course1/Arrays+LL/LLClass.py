class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.temp = None

    def addNode(self,value):

        if self.head == None:
            self.head = Node(value)
            self.temp = self.head
        else:
            self.temp.next = Node(value)
            self.temp = self.temp.next

        return
    def removeNode(self,value):
        
        if(self.head.value == value):
            self.head = self.head.next


        else:
            temp = self.head
            pre = None
            while(temp.value != value):
                pre = temp
                temp = temp.next
            pre.next = temp.next

        return

    def reverse(self):
        prev = None
        curr = self.head

        while(curr != None):

            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

def iscircular(linked_list):
    fast = linked_list.head
    slow = linked_list.head
    
    while(True):
        if(slow == None or slow.next == None or fast.next == None):
            return False
        
        slow = slow.next
        fast = fast.next.next
        if(slow == fast):
            return True
    return False

llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.addNode(value)

flipped = llist.reverse()