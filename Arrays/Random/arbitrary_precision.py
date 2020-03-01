list1 = [9,9,9]

def add_one(list1):
    carry = 0
    list1[len(list1)-1] = list1[len(list1)-1]+1
    for i in range(len(list1)-1,-1,-1):

        a = carry + list1[i]
        if a == 10:
            carry = 1
            list1[i] = 0
        elif i != (len(list1)-1):
            carry = 0
            list1[i] = a

        if list1[0] == 0:
            list1.insert(0,1)

    print(list1)
list1 = [int(i) for i in input().split()]
print(list1)
add_one(list1)
print()