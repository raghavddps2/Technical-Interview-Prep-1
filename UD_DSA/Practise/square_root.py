'''
So, in this session we are going to calculate the square root of a number using newton raphson and 
binary search method.
'''

def binary_search_square_root(n):

    low = 0.0
    high = float(n+1)

    while((high-low) > 0.000001):
        mid = (high+low)/2
        if mid*mid < n:
            low = mid
        else:
            high = mid

    #Once we are done doing the above, all we have to do is return low.
    return low

print(binary_search_square_root(float(input())))