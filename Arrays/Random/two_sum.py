
#This approach to solve the problem can be done in n^2 time
def two_sum_problem_brute_force(list1,sum):
    flag = 0
    for i in list1:
        check = sum1 - i
        if check in list1 and i != check:
            flag = 1
            print(i,check)
            
    if(flag == 0):    
        print("No such elements")

#This is an approach using the has tables and will require n time and space complexity of O(n) too

def two_sum_hash_table(lsit1,sum):
    ht = dict()
    for i in range(len(list1)):
        if list1[i] in ht.keys():
            print(ht[list1[i]],list1[i])
            return True
        else:
            ht[sum1-list1[i]] = list1[i]
    return False            

#This is simply performed in O(n) time and space complecity is also O(1)
def two_sum(list1,sum1):
    i = 0
    j = len(list1)-1
    while i<=j:
        temp = list1[i]+list1[j]
        if temp < sum1:
            i = i+1
        elif temp > sum1:
            j = j - 1
        else:
            print(list1[i],list1[j])
            return True
    return False


list1 = [int(i) for i in input("Enter the list:\t").split(" ")]
sum1 = int(input("Enter the sum:\t"))
two_sum_problem_brute_force(list1,sum1)
two_sum_hash_table(list1,sum)
print(two_sum(list1,sum1))