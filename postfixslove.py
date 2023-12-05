class stack:
    # deafult satack
    # self is used it calls it self and size will define the size of stack
    def __init__(self, size):
        self.size = size
        self.stack = [None]*size
        self.top = -1 # -1 repesents an empty stack

    # now we will create some of stack functions
    
    def stFull(self): # funcation to check the stack is full or not
        output = False
        if self.top == self.size -1:
            output = True
            print("Yes your stack is Full.")
        return output
    
    def stEmpty(self): # funcation to check the stack is empty or not
        output = False
        if self.top == -1:
            output = True
            print("Yes your stack is Empty.")
        return output
    
    def push(self,item): # funtion to push item in stack and the item is the value we have to put in stack
        if self.stFull() == False:
            self.top += 1
            self.stack[self.top] = item
            print(str(item) + " is now pushed into the stack at index " + str(self.top))
        else:
            print("Error : Your stack size if full.")
    
    def pop(self): # funcation to pop the item from the stack
        if self.stEmpty() == False:
            pop_item = self.stack[self.top]
            print(str(pop_item) + " item poped from stack from index " + str(self.top))
            self.top -= 1
            return pop_item
        else:
            print("Error: your stack is empty.")
    
    def stsize(self): # function to give the size of stack at current time
        stack_size = self.top + 1
        return stack_size

    def peek(self):
        if not self.stEmpty:
            return self.items[self.top]
        return None

stack = stack(10)

def evaluate_postfix_with_stack(expression):
    operators = set(['+', '-', '*', '/', '^'])

    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        elif char in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if operand1 is None or operand2 is None:
                return "Invalid Expression"

            if char == '+':
                stack.push(operand1 + operand2)
            elif char == '-':
                stack.push(operand1 - operand2)
            elif char == '*':
                stack.push(operand1 * operand2)
            elif char == '/':
                if operand2 == 0:
                    return "Division by zero error"
                stack.push(operand1 / operand2)
            elif char == '^':
                stack.push(operand1 ** operand2)

    result = stack.pop()
    if stack.stEmpty() and result is not None:
        return result
    else:
        return "Invalid Expression"


# Example usage:
postfix_expression = "42^3*5-"
result = evaluate_postfix_with_stack(postfix_expression)
print("Result:", result)