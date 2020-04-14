def climbingLeaderboard(scores, alice):
    res = []
    rank = 1
    scores = list(set(scores))
    for i in range(0,len(scores)):
        if i == 0:
            res.append(rank)
        else:
            if scores[i] == scores[i-1]:
                res.append(rank)
            else:
                rank = rank + 1
                res.append(rank)
    ans = []
    for i in alice:
        j = len(scores) - 1
        while scores[j] <= i and j > -1:
            j = j-1
        #corner case
        # print(j,"hi")
        if(j < 0):
            ans.append(1)
        else:
            ans.append(res[j]+1)
    return ans


def climbingLeaderboard1(scores, alice):
    for i in alice:
        j = len(scores)-1
        while scores[j] <= i:
            j = j-1
        if(j < 0):
            print(1)
        else:
            print(j)
def climbingLeaderboard2(scores, alice):
    back = len(scores) - 1
    ans = []
    for a in alice:
        while back >= 0 and a > scores[back]:
            back -= 1
        if scores[back] == a:
            ans.append(back + 1)
        else:
            ans.append(back + 2)
    return ans
scores = [100,100,50,40,40,20,10]
alice = [5,25,50,120]
print(climbingLeaderboard1(scores,alice))


