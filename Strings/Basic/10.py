T = int(input())
for _ in range(T):
    n = int(input())
    str1 = input()
    if(str1 == "".join(reversed(str1))):
        print("Yes")
    else:
        print("No")