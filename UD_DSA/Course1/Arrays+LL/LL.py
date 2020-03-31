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

    def traverse(self):
        temp = self.head
        while(temp != None):
            print(temp.value,"->",end=" ")
            temp = temp.next

        return

def main(head):

    ll = LinkedList()
    print("1. Add a new node to LL")
    print("2. Delete a new node from the LL")
    print("3. Traverse the LL")
    print("4. Exit")
    input1 = int(input("Enter the choice:\t"))
    while(input1 != 4):
        if input1 == 1:
            value = int(input("Enter the value:\t"))
            ll.addNode(value)
        elif input1 == 2:
            value = int(input("Enter the value of the node to be deleted:\t"))
            ll.removeNode(value)
        else:
            ll.traverse()
        input1 = int(input("Enter the choice:\t"))


if __name__ == "__main__":
    head = None
    main(head)