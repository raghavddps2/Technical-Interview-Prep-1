
def sort_012(array):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    count = {0:0,1:0,2:0}
    for i in array:
        if i == 0:
            count[0] = count[0]+1
        elif i == 1:
            count[1] = count[1]+1
        else:
            count[2] = count[2]+1
    arrPointer = 0
    for i in range(0,count[0]):
        array[arrPointer] = 0
        arrPointer = arrPointer + 1
    
    for i in range(0,count[1]):
        array[arrPointer] = 1
        arrPointer = arrPointer + 1
    

    for i in range(0,count[2]):
        array[arrPointer] = 2
        arrPointer = arrPointer + 1
    
    return array

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