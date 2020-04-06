import copy
def subsets(arr):
    
    if len(arr) == 0:
        return [[]]
    else:
        res = []
        temp = arr[0]
        res = subsets(arr[1:])
        for i in copy.deepcopy(res):
            i.insert(0,temp)
            res.append(i)
        return res

print(subsets([1,2]))