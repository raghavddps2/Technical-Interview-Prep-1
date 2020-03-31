def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    
    Approach:
        1. All we have to do is maintain two pointers, one for odd number and other for even numbers.
        2. Second, we just need to combine the two
    """
    if head is None:
        return head
    
    odd = None
    even = None
    odd_tail = None
    even_tail = None
    
    while(head):
        
        next_node = head.next
        if(head.data%2 == 0):
            if(even == None):
                even = head
                even_tail = even
            else:
                even_tail.next = head
                even_tail = even_tail.next
        else:
            if(odd == None):
                odd = head
                odd_tail = odd
            else:
                odd_tail.next  = head
                odd_tail = odd_tail.next
        
        head.next = None
        head = next_node
    
    if even is None:
        return odd
    if odd is None:
        return even
    odd_tail.next = even
    return odd