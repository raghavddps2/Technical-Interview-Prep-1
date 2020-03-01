T = int(input())
for i in range(T):
    a,b = input().split(" ")
    a_map = {}
    b_map = {}
    for i in a:
        if i in a_map:
            a_map[i] += 1
        else:
            a_map[i] = 1

    for i in b:
        if i in b_map:
            b_map[i] += 1
        else:
            b_map[i] = 1
    if a_map == b_map:
        print("YES")
    else:
        print("NO")