def binary_search_recursive(array, target, start_index, end_index):
    '''Write a function that implements the binary search algorithm using recursion
    
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
         
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    mid = (start_index+end_index)//2
    if(end_index < start_index):
        return -1
    if(array[mid] == target):
        return mid
    elif(array[mid] < target):
        return binary_search_recursive(array, target, mid+1,end_index)
    else:
        return binary_search_recursive(array, target, start_index,mid- 1)