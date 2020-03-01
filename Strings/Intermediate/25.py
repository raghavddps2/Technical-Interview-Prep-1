from collections import OrderedDict

n = int(input())
for _ in range(n):
    a = input()
    dict1 = OrderedDict()
    flag = 0
    for i in a:
        if i not in dict1:
            dict1[i] = 1
        else:
            print(i)
            flag = 1
            break

    if(flag == 0):
        print(-1)