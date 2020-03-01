def array_advance(list1):

    i = 0
    farthest_reach = 0
    flag = 0
    for i in range(0,len(list1)):

        print(i,farthest_reach)
        # At any point if the pointer(i), exceeds the farthest reach, it means it is stuck in a loo somewhere
        if i > farthest_reach:
            flag = 1
            break
        
        #If i is still less or equal, we can update our farthest reach easily
        farthest_reach = max(farthest_reach,list1[i]+i)
    if flag == 1:
        return False
    return True

list1 = [int(i) for i in input("Enter the list of number:\t").split(" ")]
print(array_advance(list1))