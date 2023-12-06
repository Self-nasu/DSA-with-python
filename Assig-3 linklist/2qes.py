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

    def sort_descending(self):
        if self.is_empty():
            return

        sorted_stack = Stack()
        while not self.is_empty():
            current_student = self.pop()
            while not sorted_stack.is_empty() and sorted_stack.peek().marks < current_student.marks:
                temp = sorted_stack.pop()
                self.push(temp.name, temp.marks)
            sorted_stack.push(current_student.name, current_student.marks)

        while not sorted_stack.is_empty():
            temp = sorted_stack.pop()
            self.push(temp.name, temp.marks)


def display_top_students(stack):
    if stack.is_empty():
        print("Stack is empty")
        return

    sorted_stack = Stack()
    sorted_stack = stack.sort_descending()
    count = 0
    while count < 3 and not sorted_stack.is_empty():
        student = sorted_stack.pop()
        print(f"Name: {student.name}, Marks: {student.marks}")
        count += 1


main_stack = Stack()
secondary_stack = Stack()

while True:
    print("\nMenu:")
    print("1. Add a student to the stack")
    print("2. Remove a student from the stack")
    print("3. Display all students in the stack")
    print("4. Display top 3 students")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))
        main_stack.push(name, marks)
    elif choice == '2':
        main_stack.pop()
        print("Student removed from the stack.")
    elif choice == '3':
        print("All students in the stack:")
        main_stack.display()
    elif choice == '4':
        print("Top 3 students:")
        display_top_students(main_stack)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Exiting the program.")
        break
