import math
def encryption(s):

    s = "".join(s.split())
    length = len(s)
    a = math.floor(math.sqrt(length))
    b = math.ceil(math.sqrt(length))

    all_choices = [(a,a),(a,b),(b,b)]
    min_area = 10000000000000
    for i in all_choices:
        if i[0]*i[1] >= length and i[0]*i[1] < min_area:
            min_area = i[0]*i[1]
            rows = i[0]
            columns = i[1]
            
    result_matrix = []
    j = 0
    for i in range(0,rows):
        result_matrix.append(s[j:columns+j])
        j = j + columns
    result = ""
    for i in range(columns):
        for j in result_matrix:
            if i < len(j): 
                result = result + j[i]
        result = result + " "
    print(result)
# encryption("haveaniceday")
# encryption("feedthedog    ")
# encryption("chillout")
    
import math

#beautifuuullll answer!!            
def main():
    string = input()
    char = list(string)
    # print(char)
    size = math.ceil(math.sqrt(len(string)))
    print(size)
    out = [""]*size
    print(out)
    count = 0
    for i in char:
        if count>=size:
            count = 0
        out[count]+=i
        count = count+1
    print(out)
    for j in range(len(out)):
        if j == len(out)-1:
            print(out[j])
        else:
            print(out[j], end=" ")

main()