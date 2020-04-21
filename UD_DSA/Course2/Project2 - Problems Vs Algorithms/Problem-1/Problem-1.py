import math
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    
    We will simply use the Binary search algorithm to find the square root, and we will be done in O(log(n))
    """


    low = 0.0
    high = float(number+1)

    while((high-low) > 0.000001):
        mid = (high+low)/2
        if mid*mid < number:
            low = mid
        else:
            high = mid

    return int(math.floor(high))

#Test case 1
n = 16
print("Square root of {} is: {}".format(n,sqrt(n)))

#Test case 2
n = 27
print("Square root of {} is: {}".format(n,sqrt(n)))

#Test case 3(EDGE CASE)
n = 0
print("Square root of {} is: {}".format(n,sqrt(n)))


#Outputs for the above Test cases.
# Square root of 16 is: 4
# Square root of 27 is: 5
# Square root of 0 is: 0