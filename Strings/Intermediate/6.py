T = int(input())
ans = []

def subsequences(str1,str2):
    
    if(len(str1) == 0):
        ans.append(str2)
        return
        
    subsequences(str1[1:],str2+str1[0])
    subsequences(str1[1:],str2)
    
def game(list1):
    
    str1 = ['a','e','i','o','u']
    res = []
    for i in list1:
        print(i)
        if len(i)>1:
            if i[0] in str1 and (i[len(i)-1] not in str1):
                res.append(i)
    return res 
for _ in range(T):
    a = input()
    subsequences(a,"")
    ans1 = game(ans)
    
    for i in ans1:
        print(i)