def skip_i_delete_j(head,i,j):

    if(i == 0):
        return None
    if(i < 0 or j < 0 or head is None):
        return head
    
    current = head
    previous = None

    while current:
        
        #Include first i
        for _ in range(i-1):
            if current is None:
                return head
            current = current.next
        previous = current
        current = current.next

        #Remove j
        for _ in range(j):
            if current is None:
                break
            next_node = current.next
            current = next_node
        previous.next = current
    return head

