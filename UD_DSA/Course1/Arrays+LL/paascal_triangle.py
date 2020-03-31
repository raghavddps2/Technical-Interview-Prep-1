#Wonderful: This is bases on an awesome property of pascals triangle
import math
def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    n = int(math.pow(11,n))
    return list(map(int,list(str(n))))

#The pascals triangle can also be solved by a two loop fashion.

def nth_pascal_loop(n):
    if n == 0:
        return [1]
    
    current_row = [1]
    for i in range(1,n+1):
        previous_row = current_row
        #Appending the first one
        current_row = [1]
        #This will append all values between the rows.
        for j in range(1,i):
            next_num = previous_row[j]+previous_row[j-1]
            current_row.append(next_num)
        #Appending the last one
        current_row.append(1)
    #We will simply return the current row!
    return current_row