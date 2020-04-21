def sort_012(arr):

    '''
        0 0 0 1 1 0 1 0 2 0 1 0 2 0 1
        |                           |
        low                         high
        mid

        Following are the three steps we do, as long as mid is less than high.
        1. If the value at mid index is 0, we simply replace it with the low index we have, as we have 
            zero's till that point.
        2. If the value at the mid index is 1, all we do is shift the index, and go ahead.
        3. If it is 2, we swap it with the element present at the high index and then decrease the value of high.
    '''

    low = 0
    high = len(arr)-1
    mid = 0

    while(mid <= high):

        if arr[mid] == 0:
            #We swap the values.
            arr[low],arr[mid] = arr[mid],arr[low]
            #We increase the value of low.
            low = low + 1
            #We increase the mid index.
            mid = mid + 1
        elif arr[mid] == 1:
            #We simply inc the mid index
            mid = mid + 1
        else:
            #we swap the values again.
            arr[high],arr[mid] = arr[mid],arr[high]
            high = high-1
    return arr


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

#Input 1
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])

#Input 2
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

#Input 3
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

#Input 4 (Edge case)
test_function([])

#Output
# [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
# Pass
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# Pass
# [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
# Pass
# []
# Pass
