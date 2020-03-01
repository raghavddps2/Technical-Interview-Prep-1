a = input("Enter the string:\t")
list1 = []
for i in a.split(" "):
    list1.append("".join(reversed(i)))

print(" ".join(list1))