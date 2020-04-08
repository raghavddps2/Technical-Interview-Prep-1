def longest_consecutive_subsequence(input_list):
    input_dict = dict()
    maxVal = -1
    startVal = 0
    #convert to dict
    for index,value in enumerate(input_list):
        input_dict[value] = index
    for index,value in enumerate(input_list):
        #go back to prev value and check
        if (value-1) in input_dict:
            j = (value-1)
            tempo = j
            val = 0
            #if there, start from there and keep a track
            while j in input_dict:
                j = j + 1
                val = val + 1
            #replace maxVal if greater than current val
            if val > maxVal:
                maxVal = val
                startVal = tempo
    return [i for i in range(startVal,startVal+maxVal)]
longest_consecutive_subsequence([2,2,2,2,2])           