# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLength(self,head):
        
        length = 0
        temp = head
        while(temp is not None):
            temp = temp.next
            length = length + 1
        return length
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        length = self.getLength(head)
        nodeFromFirst = length-n+1
        
        if nodeFromFirst == 1:
            return head.next
            
        
        i = 1
        current = head
        prev = None
        while(i != nodeFromFirst):
            prev = current
            current = current.next
            i = i + 1
        prev.next = current.next
        return head
        
#Can also be solved using the two pointer approach.
