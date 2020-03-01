from collections import OrderedDict 
n = int(input())

for _ in range(n):
    a = input()
    ans = ""
    b = OrderedDict()
    for i in a:
        if i not in b:
            b[i] = 1
    for k in b.keys():
        ans += k
    print(ans)
    
