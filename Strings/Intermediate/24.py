n = int(input())

for _ in range(n):
    
    a = int(input())
    b = input()
    
    b = b.split(" ")
    dict1 = {}
    for i in b:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] +=1
    
    print(dict1)