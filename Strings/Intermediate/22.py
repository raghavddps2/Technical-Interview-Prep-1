T = int(input())

for _ in range(T):
    input()
    dict1 = input().split()
    str1 = input()
    dict1 = reversed(dict1)
    # print(dict1)
    for i in dict1:
        if i in str1:
            # print(str1)
            str1 = str1.replace(i,"")
        
    if str1 == "":
        print(1)
    else:
        print(0)