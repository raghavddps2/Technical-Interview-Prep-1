import sys
def getCoins(n,coins,dp):

    #we need 0 coins for all o ruppes.
    if n == 0:
        return 0

    #Lookup
    if dp[n] != 0:
        return dp[n]

    #Rec case.
    ans = sys.maxsize
    for i in range(0,len(coins)):
        if(n-coins[i] >=0):
            subprob = getCoins(n-coins[i],coins,dp)
            ans = min(ans,subprob+1)
    dp[n] = ans
    return dp[n]
    
n = 10
dp = [0]*(n+1)
print(getCoins(n,[2,3,5,6],dp))
print(dp)