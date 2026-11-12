class Student():

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll


    def get_name(self): # getter method :- It return the value of instance variable
        return self.name


    def get_roll(self):
        return self.roll


s1 = Student("Yash",101)

print(f"Studen Name : {s1.get_name()}")

print(f"Student Roll Number : {s1.get_roll()} ")
        