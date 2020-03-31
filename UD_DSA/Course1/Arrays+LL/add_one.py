def add_one(arr):
    arr[-1] = arr[-1]+1
    carry = 0
    for i in range(len(arr)-1,-1,-1):
        arr[i] = arr[i]+carry
        if(arr[i] >= 10):
            arr[i] = arr[i]%10
            carry  = 1

    if(carry == 1):
        arr.insert(0,1)

arr = [9,9,9]
add_one(arr)
print(arr)