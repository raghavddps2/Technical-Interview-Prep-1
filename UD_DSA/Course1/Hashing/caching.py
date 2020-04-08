dict1 = dict()
def staircase(n):
    
    if n in dict1:
        return dict1[n]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        a = staircase(n-1)
        dict1[n-1] = a
        b = staircase(n-2)
        dict1[n-2] = b
        c = staircase(n-3)
        dict1[n-3] = c
        return a + b + c
    pass