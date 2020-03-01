word_map = {}
str1 = input("Enter the string:\t")

for i in str1:
    if i != " ":
        if i in word_map:
            word_map[i] += 1
        else:
            word_map[i] = 1

print("The character and the occurences are ")
for i in word_map:
    print(i,word_map[i])

