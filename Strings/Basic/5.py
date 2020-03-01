str1 = input("Enter the string:\t")

#In-place means that you should update the original string rather than creating a new one
n = len(str1)
str1 = list(str1)
for i in range(n//2):
    temp = str1[i]
    str1[i] = str1[n-i-1]
    str1[n-i-1] = temp

print("".join(str1))
