def binarySearch(array,target):

    low = 0
    high = len(array)-1

    while(low <= high):
        mid = (low+high)//2
        if array[mid] < target:
            low = mid+1
        elif array[mid] == target:
            return mid
        else:
            high = mid-1
    return -1

def rotated_array_search(nums,target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    left = 0
    right = len(nums)-1
        
    while(left < right):
            
        mid = (left+right)//2
            
        if(nums[mid] > nums[right]):
            left = mid + 1
        else:
            right = mid
                
    pivot = left
    #Now, once we obtain the pivot, we have to decide,
    # which array to apply binary search for, left or right.
    # print(pivot)
    arr1_start = pivot
    arr1_end = len(nums)-1

    arr2_start = 0
    arr2_end = pivot-1

    if(target >= nums[arr1_start] and target <= nums[arr1_end]):
        print("array1",nums[arr1_start:arr1_end+1])
        ans1 =  binarySearch(nums[arr1_start:arr1_end+1],target)
        if ans1 == -1:
            return -1
        else:
            return (arr1_start+ans1)
    else:
        print("array2",nums[arr2_start:arr2_end+1])
        return binarySearch(nums[arr2_start:arr2_end+1],target)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    print("Index: ",rotated_array_search(input_list, number))
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Test case 1
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
#Test case 2
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
#Test case 3
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
#Test case 4
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
#Test case 5
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

#Ouputs:
# array2 [6, 7, 8, 9, 10]
# Index:  0
# array2 [6, 7, 8, 9, 10]
# Pass
# array1 [1, 2, 3, 4]
# Index:  5
# array1 [1, 2, 3, 4]
# Pass
# array2 [6, 7, 8]
# Index:  2
# array2 [6, 7, 8]
# Pass
# array1 [1, 2, 3, 4]
# Index:  3
# array1 [1, 2, 3, 4]
# Pass
# array2 [6, 7, 8]
# Index:  -1
# array2 [6, 7, 8]
# Pass