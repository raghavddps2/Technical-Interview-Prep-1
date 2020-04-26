def subsetSum(sum,n,arr):

    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    if arr[n-1] <= sum:
        a1 = subsetSum(sum-arr[n-1],n-1,arr)
        a2 = subsetSum(sum,n-1,arr)
        return a1 or a2
    else:
        return subsetSum(sum,n-1,arr)

sum = [2,2,7,8,10]
a = 34
print(subsetSum(a,len(sum),sum))