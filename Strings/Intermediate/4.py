n = int(input())
def pallin(a):
    if a == a[::-1]:
        return (True,a)
    else:
        return (False,a)

for _ in range(n):
    
    a = input()
    lst = []
    for i in range(0,len(a)):
        for j in range(i+1,len(a)+1):
            lst.append(a[i:j])

    ans1 = [pallin(ref) for ref in lst]
    ans2 = []
    for i in ans1:
        if i[0] == True:
            ans2.append(i[1])

    ans3 = ""
    max = 0
    for i in ans2:
        if len(i) > max:
            ans3 = i
            max = len(ans3)
    print(ans3)
    