def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    sum1 = 0
    for i in range(0,len(arr)-1):
        sum1 = sum1+i
    sum2 = sum(arr)
    return sum2-sum1
    