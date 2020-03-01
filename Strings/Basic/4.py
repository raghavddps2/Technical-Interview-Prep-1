str1 = input("Enter the string:\t")

map1 = {}
list1 = []
for i in str1:
    if i in map1:
        list1.append(i)
    else:
        map1[i] = 1

print("THe duplicate characters are:\t",list1)