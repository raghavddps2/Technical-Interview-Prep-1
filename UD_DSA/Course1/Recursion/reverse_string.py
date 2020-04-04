# Code

def reverse_string(input):
    if(input == ""):
        return ""
    
    if(len(input) == 1):
        return input
    else:
        str1 = input[len(input)-1]
        str1 = str1 + reverse_string(input[0:len(input)-1])
        return str1
    
reverse_string("abcd")

# Test Cases
    
print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")