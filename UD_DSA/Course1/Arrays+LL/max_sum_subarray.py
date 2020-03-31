def max_sum(arr):

    max_sum = arr[0]
    curr_sum = arr[0]

    for i in arr[1:]:

        curr_sum = max(curr_sum+i,i)
        max_sum = max(max_sum,curr_sum)
    return max_sum

arr = [1,-4,-5,-6,7,-7]
print(max_sum(arr))