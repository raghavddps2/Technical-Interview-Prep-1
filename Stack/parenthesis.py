import stack
st = stack.stack()


def checkBalanced(expression):
    i = 0
    while(i<len(expression)):
        a = expression[i]
        if a == '(' or a == '{' or a == '[':
            st.push(expression[i])
        
        if a == ')' or a == '}' or a == ']':
            if a == ')':
                if st.peek() == '(':
                    st.pop()
                else:
                    return False
            if a == '}':
                if st.peek() == '{':
                    st.pop()
                else:
                    return False

            if a == ']':
                if st.peek() == '[':
                    st.pop()
                else:
                    return False
        print(st.items)
        i = i+1

    if st.size() == 0:
        return True
    else:
        return False


#This takes the input for the expression
expression = input("Enter the expression:\t")
print("Bracket is balanced:\t",checkBalanced(expression))


