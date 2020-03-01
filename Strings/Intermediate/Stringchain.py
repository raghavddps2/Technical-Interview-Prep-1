"""
    The task in this question is to basically determine the longest string chain
"""

def solution(words):
    words.sort(key=len)
    dictionary = dict()

    for word in words:
        dictionary[word] = 1 + max(dictionary.get(word[:j]+word[j+1:],0) for j in range(len(word)))
    
    return max(dictionary.values())

words = ['a','and','an','bear']
print(solution(words))