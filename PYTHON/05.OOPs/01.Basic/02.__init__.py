class Student:
    def __init__(self):
        self.name = "Yash"
        self.roll = 7

    def display(self):
        print(f"My name is {self.name} and roll number is {self.roll}")

s1 = Student()
s1.display()