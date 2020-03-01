for _ in range(int(input())):
    n = int(input())
    s1 = int(n*(n+1)/2)
    arr = input().split()
    arr = list(map(int,arr))
    print(s1-sum(arr))