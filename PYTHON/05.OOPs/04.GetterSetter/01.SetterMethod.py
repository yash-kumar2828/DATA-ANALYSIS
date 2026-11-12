class Student():

    def __init__(self,name,phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def set_name(self,name): # setter method :- it is mdify or update tha value of instance variable
        self.name = name

    def set_phoneNumber(self,phoneNumber): # setter method :- it is mdify or update tha value of instance variable
        self.phoneNumber = phoneNumber


    def display(self):
        print(f"My name is : {self.name}")
        print(f"My phone number is : {self.phoneNumber}")


s1 = Student("Yash",7631659415)

s1.display()
print()

s1.set_name("Yash Kumar")
s1.set_phoneNumber(9771361567)
s1.display()
        