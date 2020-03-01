import stack
def reverse(expression):
    st = stack.stack()
    for i in expression:
        st.push(i)
    st.items.reverse()
    return "".join(st.items)

expression  = input("Enter the string:\t")
print("The reversed string is:\t",reverse(expression))
