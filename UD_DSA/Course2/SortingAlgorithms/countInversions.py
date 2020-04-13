inversions = 0
def mergesort(items):
    
    if len(items) <=1:
        return items

    mid_point = len(items)//2

    left = mergesort(items[0:mid_point])
    right = mergesort(items[mid_point:])

    return merge(left,right)

def count_inversions(items):
    global inversions
    inversions = 0
    mergesort(items)
    return inversions

def merge(left,right):
    global inversions
    i = 0
    j = 0
    ans = []
#     print(left,right)
    while i<len(left) and j<len(right):
#         print(left[i],right[i])
        if left[i] <= right[j]:
            ans.append(left[i])
            i = i + 1
        else:
            inversions = inversions + len(left[i:])
            ans.append(right[j])
            j = j + 1

    if i < len(left):
        ans.extend(left[i:])
    if j < len(right):
        ans.extend(right[j:])
    
    return ans

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    print(count_inversions(arr))
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")

arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)
