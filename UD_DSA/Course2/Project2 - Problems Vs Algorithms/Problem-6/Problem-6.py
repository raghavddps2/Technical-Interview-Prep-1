import sys

def get_min_max(ints):

    if (len(ints) == 0):
        print("Array is empty!")
        return -1

    maximum = -sys.maxsize
    minimum = sys.maxsize

    for i in ints:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    
    print("Maximum minimum pair is: ",(minimum,maximum))
    return (minimum,maximum)

## Example Test Case of Ten Integers
import random

#Test case 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

#Test case 2 (Edge case)
l = [1,1,1,1,1,1,1,1,1,1,1,1,]
print ("Pass" if ((1,1) == get_min_max(l)) else "Fail")

#Test case 3 (Empty array)(Edge)
l = []
print ("Pass" if (-1 == get_min_max(l)) else "Fail")

#Test case 4 
l = [2,5,1,4,8,9,56,76,43,56,7,8,9,6,4]
print ("Pass" if ((1,76) == get_min_max(l)) else "Fail")

# Output
# Maximum minimum pair is:  (0, 9)
# Pass
# Maximum minimum pair is:  (1, 1)
# Pass
# Array is empty!
# Pass
# Maximum minimum pair is:  (1, 76)
# Pass