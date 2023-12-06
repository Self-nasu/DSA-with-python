# Reusing the Stack class you provided
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

    def peek(self):
        if not self.stEmpty():
            return self.stack[self.top]
        return None

# Function to sort the stack using another temporary stack
def sort_stack(stack):
    temp_stack = Stack(stack.size)

    while not stack.stEmpty():
        temp = stack.pop()

        # Move items from temporary stack to main stack that are greater than temp
        while not temp_stack.stEmpty() and temp_stack.peek() > temp:
            stack.push(temp_stack.pop())

        temp_stack.push(temp)

    # Moving elements back to the main stack
    while not temp_stack.stEmpty():
        stack.push(temp_stack.pop())

# Example usage
stack = Stack(8)
stack.push(4)
stack.push(2)
stack.push(5)
stack.push(1)
stack.push(3)

print("Stack before sorting:")
while not stack.stEmpty():
    print(stack.pop(), end=" ")

sort_stack(stack)

print("\nStack after sorting:")
while not stack.stEmpty():
    print(stack.pop(), end=" ")
