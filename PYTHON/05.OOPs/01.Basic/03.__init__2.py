class Student:
    def __init__(self,x,y):
        self.name = x
        self.roll = y

    def display(self):
        print(f"My name is {self.name} and roll number is {self.roll}")

s1 = Student("Yash",6)
s2 = Student("Kumar",4)

s1.display()
s2.display()