import stack

st = stack.stack()

def decimalToBin(number):

    while number != 1:
        a = number%2
        st.push(str(a))
        number = number//2
    st.push(str(number))
    st.items.reverse()
    return "".join(st.items)

number = int(input("Enter the number:\t"))
print("The binary equivalent is:\t",decimalToBin(number))