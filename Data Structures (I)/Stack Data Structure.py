# Stack implementation in python


# Creating a stack
def create_stack():
    stack = []
    return stack


# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0


# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))

#-------------------------------------------------------------------------------------------------------------------

# Applications of Stack Data Structure
# Although stack is a simple data structure to implement, it is very powerful. 
# The most common uses of a stack are:

# To reverse a word - Put all the letters in a stack and pop them out. 
# Because of the LIFO order of stack, you will get the letters in reverse order.

# In compilers - Compilers use the stack to calculate the value of expressions like 
# 2 + 4 / 5 * (7 - 9) by converting the expression to prefix or postfix form.

# In browsers - The back button in a browser saves all the URLs you have visited previously in a stack. 
# Each time you visit a new page, it is added on top of the stack. 
# When you press the back button, the current URL is removed from the stack, and the previous URL is accessed.



