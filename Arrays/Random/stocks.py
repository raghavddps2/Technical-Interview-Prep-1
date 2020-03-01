
def stock(list1):
    
    max1 = 0
    buy_day = 0
    sell_day = 0
    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            temp = list1[j] - list1[i]
            if temp > max1:
                max1 = temp
                buy_day = i
                sell_day = j

    
    print("Buy Date:\t",buy_day)
    print("Sell Date:\t",sell_day)
    print("Profit:\t",max1)

list1 = [310,315,275,295,260,270,290,230,255,250]
stock(list1)