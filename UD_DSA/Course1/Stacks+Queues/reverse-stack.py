#This is a beautiful, beautiful question.
from stack_ll import Stack
    
def reverse_stack(stack):
    holder_stack = Stack()
    while not stack.is_empty():
        popped_element = stack.pop()
        holder_stack.push(popped_element)
    _reverse_stack_recursion(stack,holder_stack)

def _reverse_stack_recursion(stack,holder_stack):
    if holder_stack.is_empty():
        return
    popped_element = holder_stack.pop()
    _reverse_stack_recursion(stack,holder_stack)
    stack.push(popped_element)


'''
Approach:
    1. Maake a new stack
    2. Get the elements in that stack.
    3. Now, the element at the bottom of stack one is at the top of stack two.
    4. Next, what we have to do is, basically, reverse_the_stack using recursion.
    5. This will result in the proper reversed stack.
'''