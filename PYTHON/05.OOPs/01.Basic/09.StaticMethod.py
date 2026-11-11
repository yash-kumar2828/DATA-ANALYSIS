class Student():

    InstituteName = "QSpider"

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def display(self): # Instance Method
        print(f"Name : {self.name} & Roll : {self.roll}")


    @classmethod
    def InstituteInfo(cls): # Class Method 
        print(f"Institute Name : {cls.InstituteName}")


    @staticmethod
    def SumOfDigit(): # Static Method :- It is not related to instance variable or static variable
        num = int(input("Enter the number :"))
        sum = 0
        while num>0:
            rem = num%10
            sum+=rem
            num//=10
        print(f"Sum of digit is : {sum}")


s1 = Student("Yash",101)
s1.display()
s1.InstituteInfo()
s1.SumOfDigit()
