def merge(left,right):

    #ALl we are doing is merging the two arrays simply!
    i = 0
    j = 0
    ans = []
    while i<len(left) and j< len(right):
        if left[i] <= right[j]:
            ans.append(left[i])
            i = i+1
        elif left[i] > right[j]:
            ans.append(right[j])
            j = j + 1
        else:
            continue
    if i == len(left):
        ans.extend(right[j:])
    if j == len(right):
        ans.extend(left[i:])
    return ans

def merge_sort(arr):

    if(len(arr) <=1):
        return arr
    
    mid_point  = len(arr)//2
    left = merge_sort(arr[0:mid_point])
    right = merge_sort(arr[mid_point:])
    return merge(left,right)

def case_sort(string1):

    arr = [ord(i) for i in string1]
    # print(arr)
    arr = merge_sort(arr)
    # print(arr)
    result = ""
    for a in arr:
        result = result + chr(a)
    # print(result)

    lower = ""
    upper = ""
    for i in range(0,len(arr)):
        if arr[i] >=97:
            lower = result[i:]
            upper = result[:i]
            break
    output = ""
    ref1 = 0
    ref2 = 0
    for i in string1:
        if i.islower():
            output = output + lower[ref1]
            ref1 = ref1 + 1
        else:
            output = output + upper[ref2]
            ref2 = ref2 + 1
    return output


print(case_sort("fedRTSersUXJ"))

