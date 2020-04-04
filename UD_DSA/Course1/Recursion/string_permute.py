import copy
def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    res = []
    if string == "":
        return [""]
    else:
        first = string[0]
        remain  = string[1:]
        sub = permutations(remain)
        for p in sub:
            for j in range(len(p)+1):
                r = copy.deepcopy(p)
                s = r[0:j]+first+r[j:]
                res.append(s)
        return res
permutations("abc")