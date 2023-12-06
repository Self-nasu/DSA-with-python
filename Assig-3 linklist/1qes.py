class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, name, marks):
        new_student = Student(name, marks)
        if self.is_empty():
            self.top = new_student
        else:
            new_student.next = self.top
            self.top = new_student

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            popped_student = self.top
            self.top = self.top.next
            popped_student.next = None
            return popped_student

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.top

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            current_student = self.top
            while current_student:
                print(f"Name: {current_student.name}, Marks: {current_student.marks}")
                current_student = current_student.next

stack = Stack()
stack.push("Naman", 90)
stack.push("Riya", 85)
stack.push("BhanuPartap", 80)

print("Stack contents:")
stack.display()

print("\nPeek:")
top_student = stack.peek()
if top_student:
    print(f"Top Student: {top_student.name}, Marks: {top_student.marks}")

print("\nPop:")
popped_student = stack.pop()
if popped_student:
    print(f"Popped Student: {popped_student.name}, Marks: {popped_student.marks}")

print("\nStack contents after pop:")
stack.display()
