# https://www.youtube.com/watch?v=4jY57Ehc14Y
# Use the above link while revising
def computeLPSArray(pattern,m,lps):

    len = 0
    i = 1

    #There will be no suffix of this prefix
    lps[0] = 0 

    while i < m:
        # print("holo1")
        if pattern[i] == pattern[len]:
            lps[i] = len + 1
            i = i + 1
            len = len + 1
        else:
            if len != 0:
                len = lps[i-1]
                i = i + 1
            else:
                len = 0
                lps[i] = 0
                i = i + 1

def KMPSearch(text,pattern):

    N = len(text)
    M = len(pattern)

    #This will be our longest prefix suffix array.
    lps = [0]*M 
    # print("holo")
    computeLPSArray(pattern,M,lps)

    i = 0 #Pointer for the text
    j = 0 #Pointer for the pattern

    while i < N:
        if text[i] == pattern[j]:
            i = i + 1
            j = j + 1
        else:
            if j != 0:
                #Because we got a match till j-1
                j = lps[j-1]
            else:
                #If this happens, all we have to do is increment i.
                i = i + 1
        # print("hi")
        if j == M:
            #We have came to the end of the pattern
            print(i-j)
            #We will again reset j to lps of (j-1)
            j = lps[j-1]

#This algorithm is applied a lot in case when we have DNA sequence mathcing.
KMPSearch("mississippi","issipi")