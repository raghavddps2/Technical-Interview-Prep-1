n = int(input())

for i in range(n):
    str1 = input()
    str2 = input()
    
    if len(str1) != len(str2):
        print(0)
        continue
    
    else:
        str1 = str1 + str1
        if str2 in str1:
            print(1)
        else:
            print(0)
