
def merge_lists(my_list1,my_list2):

    # Combine the sorted lists into one large sorted list
    ans = []
    
    i = 0
    j = 0
    
    while i < len(my_list1) and j< len(my_list2):
        
        if my_list1[i] < my_list2[j]:
            ans.append(my_list1[i])
            i = i+1
        
        elif my_list1[i] > my_list2[j]:
            ans.append(my_list2[j])
            j = j+1
        
        else:
            ans.append(my_list1[i])
            ans.append(my_list1[i])
            i = i+1
            j = j+1

        print(ans,i,j)

    while i < len(my_list1):
        ans.append(my_list1[i])
        i = i+1
    
    while j < len(my_list2):
        ans.append(my_list2[j])
        j = j+1

    return ans

print(merge_lists([2, 4, 6], [1, 3, 7]))