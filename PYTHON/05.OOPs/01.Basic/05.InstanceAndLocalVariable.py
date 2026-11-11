class Student():

    def __init__(self,x,y): # x,y are local variable
        self.name = x   # name is instance variable
        self.roll = y   # roll is instance variable


    def display(self):
        print(f"Name : {self.name} & Roll : {self.roll}")


s1 = Student("Yash",101)
s1.display()
        