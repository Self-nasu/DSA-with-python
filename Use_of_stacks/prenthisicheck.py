class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def stFull(self):
        return self.top == self.size - 1

    def stEmpty(self):
        return self.top == -1

    def push(self, item):
        if not self.stFull():
            self.top += 1
            self.stack[self.top] = item

    def pop(self):
        if not self.stEmpty():
            pop_item = self.stack[self.top]
            self.top -= 1
            return pop_item
        return None

# Function to check parentheses matching using the provided Stack class
def check_parentheses(expression):
    stack = Stack(len(expression))

    # Dictionary to map opening and closing parentheses
    parentheses = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in parentheses.keys():  # If it's an opening parentheses
            stack.push(char)
        elif char in parentheses.values():  # If it's a closing parentheses
            if stack.stEmpty() or parentheses[stack.pop()] != char:
                return False  # Mismatched or no opening parentheses found
    return stack.stEmpty()  # If stack is empty, all parentheses matched

# Example usage
input_expression = "{[5 * (2 + 3)] / (4 - 1)}"
if check_parentheses(input_expression):
    print("The parentheses in the expression are correctly matched.")
else:
    print("The parentheses in the expression are not correctly matched.")
