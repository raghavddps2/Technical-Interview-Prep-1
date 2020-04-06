def last_index_rec(arr,target,index):
    
    if index < 0:
        return -1
    if arr[index] == target:
        return index
    return last_index_rec(arr,target,index-1)
def last_index(arr, target):
    return last_index_rec(arr,target,len(arr)-1)
    
print(last_index([1,1,2,3,4,1],1))