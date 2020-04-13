def mergeSort(items):

    #The base case, when number of elements is less than or equal to 1,
    #implies it is sirted hence, we return.
    if len(items) <=1:
        return items

    #We find the mid point for the array.
    mid_point = len(items)//2
    #We get the left half of the array
    left = items[0:mid_point]
    #We find the right half of the array
    right = items[mid_point:]

    #We call merge sort on left and right half.
    left = mergeSort(left)
    right = mergeSort(right)

    #NOw, all we have to do is to merge the right and the left half.
    return merge(left,right)

def merge(left,right):

    #ALl we are doing is merging the two arrays simply!
    i = 0
    j = 0
    ans = []
    while i<len(left) and j< len(right):
        if left[i] < right[j]:
            ans.append(left[i])
            i = i+1
        elif left[i] >= right[j]:
            ans.append(right[j])
            j = j + 1
        else:
            continue
    if i == len(left):
        ans.extend(right[j:])
    if j == len(right):
        ans.extend(left[i:])
    return ans

print(mergeSort([9,8,7,6,5,4,3,2,1]))