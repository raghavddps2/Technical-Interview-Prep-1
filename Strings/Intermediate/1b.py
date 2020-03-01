n = int(input())

for i in range(n):
    str1 = input()
    str2 = input()
    
    if len(str1) != len(str2):
        print(0)
        continue;
    
    else:
        a = str2[0]
        flag = 0
        indexes = [i for i,ltr in enumerate(str1) if ltr1 == a]
        for n in indexes:
            loc1 = str1[n:]
            loc1 = loc1 + str1[:n]
            # print(loc1)
            if(loc1 == str2):
                print(1)
                flag = 1
                continue;
        if(flag == 0):
            print(0)
