def isSubset(array,num_elements,sum):
    # print(sum,num_elements)
    dp = [[0]*(sum+1)]*(num_elements+1)
    for i in range(0,(sum+1)):
        dp[0][i] = False
    for i in range(0,(num_elements+1)):
        dp[i][0] = True

    for i in range(1,(num_elements+1)):
        for j in range(1,(sum+1)):

            if(array[i-1] <= j):
                dp[i][j] = (dp[i-1][j] or dp[i-1][j-array[i-1]])
            else:
                dp[i][j] = dp[i-1][j]

    print(dp)
    return dp[num_elements][sum]
    
def subset_sum_problem(array,n):
    
    if sum(array)%2 != 0:
        return False
    else:
        a =  isSubset(array,n,sum(array)//2)
        # print(a)
        return a

q = int(input())
for _ in range(0,q):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = subset_sum_problem(arr,n)
    if(ans == True):
        print("YES")
    else:
        print("NO")