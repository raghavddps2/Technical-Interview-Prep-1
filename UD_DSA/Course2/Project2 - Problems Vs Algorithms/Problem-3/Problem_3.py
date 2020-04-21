import random
def get_two_numbers(array):

    '''
    1. If, the length of the array is even, then it is traight forward, to get the maximum sum, all
        we have to do is make numbers from alternating elements of the array.
        One important reasoning behind this is that, as stated in the problem,
        the maximum difference between the digits of two numbers can be one.

    2. If the length of the array is odd and just one, we simply return that array.
        If it is greater than one, all we have to do is combine alternately and stop when exhausted.
        I can actually make that one same case.
    '''
    if len(array) == 1:
        return array
    else:

        element1 = ""
        element2 = ""

        for i in range(0,len(array)):
            if(i%2 == 0):
                element1 = element1 + str(array[i])
            else:
                element2 = element2 + str(array[i])
    return [int(element1),int(element2)]
def merge_sort(array):

    '''
    Concept of merge sort:
    
        1. Base case: 
            Go on dividing the array until its size if greater than 1.
        2. Recursive functions
            Split the array into two left and right half.
            call merge sort recursively on both the halves.
        3. Merge the two arrays.

    '''
    # print("hi")
    if len(array) == 1:
        return array
    
    else:
        mid = len(array)//2
        left = array[0:mid]
        right = array[mid:]

        left_sorted = merge_sort(left)
        right_sorted = merge_sort(right)

        return merge(left_sorted,right_sorted)

def merge(left_array,right_array):

    ''' 
        Concept of the merge function.

        1. Iterate on both elements till elements
            exist in both the arrays and store them in a 
            result array in sorted fashion.
        2. When any of the array is exhausted, go on filling
            the result array with tthe array that is not exhausted.

    '''

    i = 0
    j = 0
    result_arr = []
    while(i<len(left_array) and j<len(right_array)):

        if left_array[i] > right_array[j]:
            result_arr.append(left_array[i])
            i = i + 1
        else:
            result_arr.append(right_array[j])
            j = j + 1
    # print("hiff")
    #if left is NOT exhausted.
    while(i < len(left_array)):
        result_arr.append(left_array[i])
        i  = i+1
    
    #if right is NOT exhausted.
    while(j < len(right_array)):
        result_arr.append(right_array[j])
        j = j+1
    return result_arr

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_array = merge_sort(input_list)
    ans =  get_two_numbers(sorted_array)
    print("Two integers that can be formed are: ",ans)
    return ans


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test case 1
test_function([[1, 2, 3, 4, 5], [542, 31]])

#Test case 2
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

#Test case 3 (Edge case)
test_function([[1],[1]])

#Test case 4 
l = [i for i in range(0, 9)]  # a list containing 0 - 999
random.shuffle(l) #Shuffling for unsorting it
test_function([l, [86420, 7531]])



# Outputs
# Two integers that can be formed are:  [531, 42]
# Pass
# Two integers that can be formed are:  [964, 852]
# Pass
# Two integers that can be formed are:  [1]
# Pass
# Two integers that can be formed are:  [86420, 7531]
# Pass