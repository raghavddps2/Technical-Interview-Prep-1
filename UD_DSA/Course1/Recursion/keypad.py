def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return " "


def keypad(num):
    
    if(num == 0):
        return['']
    else:
        res = []
        temp = get_characters(num%10)
        arr = keypad(num//10)
        for i in temp:
            for j in arr:
                res.append((j+i))
        return res