queries = int(input())

for _ in range(0,queries):
    N = int(input())
    W = int(input())
    values = list(map(int,input().split()))
    weights = list(map(int,input().split()))
    
    #First step is we make a DP array.
    dp = [[0 for x in range(W + 1)] for x in range(N + 1)]
    print(dp)
    #First step is to make all the rows with column 0 and rows 0 as -1
    for n in range(0,(N+1)):
        for w in range(0,(W+1)):

            if n == 0 or w == 0:
                dp[n][w] = 0
            elif weights[n-1] <= w:
                dp[n][w] = max(values[n-1]+dp[n-1][W-weights[n-1]],dp[n-1][w])
            else:
                dp[n][w] = dp[n-1][w]
    print(dp)
    print(dp[N][W])

