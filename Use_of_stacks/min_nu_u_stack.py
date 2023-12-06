class MinStack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1
        self.min_stack = [float('inf')] * size  # Initializing min_stack with max value

    def stFull(self):
        return self.top == self.size - 1

    def stEmpty(self):
        return self.top == -1

    def push(self, item):
        if not self.stFull():
            self.top += 1
            self.stack[self.top] = item
            if self.top == 0:
                self.min_stack[self.top] = item
            else:
                self.min_stack[self.top] = min(item, self.min_stack[self.top - 1])

    def pop(self):
        if not self.stEmpty():
            pop_item = self.stack[self.top]
            self.top -= 1
            return pop_item
        return None

    def minimum(self):
        if not self.stEmpty():
            return self.min_stack[self.top]
        return None

# Example usage
stack = MinStack(10)
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(1)

print("Minimum element in the stack:", stack.minimum())  # Output: 1

stack.pop()
print("Minimum element in the stack after pop operation:", stack.minimum())  # Output: 2
