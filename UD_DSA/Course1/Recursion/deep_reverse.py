
def deep_reverse(arr,res):

    '''
        Base case: Here, as soon as the list is over, we return,
    '''
    if(len(arr) == 0):
        return
    else:
        '''
            1. We take the element from the end of the list
                i). If it is a list, we recursively call the same function on this element(list) and
                then append to the result array.
                ii) If not a list, all we have to do is append the current element and call recursion on the remaining list.
            2. After this, we just have to return the result.
        '''
        temp = arr[len(arr)-1]

        #If the element is of type list, do this.
        if(type(temp) is list):
            res1 = []
            deep_reverse(temp,res1)
            res.append(res1)
        #else, just append to the res array.
        else:
            res.append(temp)
        #Now, we call recursion again.
        deep_reverse(arr[0:len(arr)-1],res)

        
        
    return res

#Test on these.
print(deep_reverse([1,2,3,4,5],[]))
print(deep_reverse([1, [2, 3, [4, [5, 6]]]],[]))

#Ouput
[5,4,3,2,1]
[[[[6, 5], 4], 3, 2], 1]