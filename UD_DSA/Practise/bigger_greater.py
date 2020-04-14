#Getting the next lexicographically greater string.
def next_lexicographic(string):

    ''' 

        Algorithm:
            1. Check when a character is less than immediate next character from the end.
                i) Now, once you find this character, it means all the chars to its right
                    are greater than that
            2. Now, we will replace this character with the one neareast available from the end.
                i) replace the character with that simply, that is greater than the smallest one.
            3. Once done, all we have to do is to sort the characters from (k+1) till the end.!


    '''
    #This gives you the index of character that is less than its immediate character,
    #if k remains still -1, it means entire string is in descending order and we cant have a 
    #next lexicographically greater string.
    k = -1
    for j in range(len(string)-2,-1,-1):
        if string[j] < string[j+1]:
            k = j
            break
    
    #if k still remains -1, it means purely descending.
    if (k == -1):
        return "no answer"

    #This step, i replace the bigger character from the end with the less one i found in the previous step
    string = list(string)
    for j in range(len(string)-1,-1,-1):
        if string[k] < string[j]:
            string[k],string[j] = string[j],string[k]
            break
    
    #Now, as all the K are basically greater than string[k] and we interchanged the required indexes, 
    #to better the result, all we have to do is sorting.
    string[k+1:] = string[k+1:][::-1]
    return "".join(string)

t = int(input())
for _ in range(t):
    print(next_lexicographic(input()))
    
