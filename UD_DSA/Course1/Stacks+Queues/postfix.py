from stack_ll import Stack
def evaluate_post_fix(input_list):
    """
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """
    stack = Stack()
    for i in input_list:
        if i == '+':
            num1 = stack.pop()
            num2 = stack.pop()
#             print(num1+num2)
            stack.push(num1+num2)
        elif i == '-':
            num1 = stack.pop()
            num2 = stack.pop()
#             print(num2-num1)
            stack.push(num2-num1)
        elif i == '*':
            num1 = stack.pop()
            num2 = stack.pop()
#             print(num1*num2)
            stack.push(num1*num2)
        elif i == '/':
            num1 = stack.pop()
            num2 = stack.pop()
#             print(num2//num1)
            stack.push(int(num2/num1))
        else:
            stack.push(int(i))
    return stack.pop()