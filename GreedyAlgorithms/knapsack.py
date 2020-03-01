"""
    Problem: Fractional Knapsack
    Algorithm:
        1. The first step in the knapsack problem is to find the value by weight ratio for each of the item.
        2. The item with the maximum vallue/weight ratio is taken into account.
        3. At each step, we keep on decreasing the sack capacity
        4. Now, if we have capacity left and we cannot fit an entire item, what we do is, we basically, add a fraction of the item to the sack.
    
    Sample Input:
        2
        3 50
        60 10 100 20 120 30
        2 50
        60 10 100 20
    
    Sample Output:
        240.00
        160.00
"""


import copy
T = int(input())

for t in range(0,T):
    
    #Line numbers 28 to 34 just help in taking the inputs from the user and foring the respective weight and values array.
    value = []
    weight = []
    n,W = list(map(int,input().split(" ")))
    temp = input().split(" ")
    for i in range(0,len(temp)-1,2):
        value.append(int(temp[i]))
        weight.append(int(temp[i+1]))


    #Second crucial thing is we will calculate the value_by_weight ratio.
    value_by_weight = []
    
    #Once, we are done taking the value by weight ratio, all we have to do is, take the one with the max ratio.
    #This is the simple strategy we need to follow.

    for i in range(0,len(value)):
        value_by_weight.append(value[i]/weight[i])
    
    #We create the deep copy just to keep track as to how many items are processed.
    tempo = copy.deepcopy(value_by_weight)

    #This is to store what fraction of the item is used.
    fraction = [0 for i in range(0,len(weight))]

    #Here, is our actual logic.
    while W > 0 and len(tempo) > 0:
        max1 = -1
        local = -1

        #This loop gives us the max everytime.
        for i in range(0,len(value_by_weight)):
            if value_by_weight[i] > max1:
                max1 = value_by_weight[i]
                local = i
        
        #Here, we calculate, if greater, we put once as the required fraction.
        if W-weight[local] >= 0:
            fraction[local] = 1
        else:
            fraction[local] = W/weight[local]
            W = 0
        W = W - weight[local]
        tempo.remove(max1)
        value_by_weight[local] = -1
    

    #Now, alll we have to do is calculate the price according to the fractions and print it upto two decimal places.
    ans = 0
    for i in range(0,len(fraction)):
        ans = ans + fraction[i]*value[i]
    print("%0.2f"%ans)