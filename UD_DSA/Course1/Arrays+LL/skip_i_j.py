def skip_i_delete_j(head,i,j):

    #Always right the edge cases, if i==0, nothing to include, return None
    if(i == 0):
        return None

    #If anything less than zero or head is None simply return head.
    if(i < 0 or j < 0 or head is None):
        return head
    
    # Assign current to head and precious to None
    current = head
    previous = None

    #While curren exists
    while current:
        #Include first i
        for _ in range(i-1):
            if current is None:
                return head
            current = current.next
        
        #We mark the previous and shift the current
        previous = current
        #We shift the crrent to the next node.
        current = current.next

        #Remove j 
        for _ in range(j):
            if current is None:
                break

            next_node = current.next
            current = next_node
        #Assign to previou's head.
        previous.next = current
    return head

