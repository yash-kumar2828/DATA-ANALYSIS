class Student():

    InstituteName = "QSpider" # Static Variable

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def display(self): # Instance Method
        print(f"Name : {self.name} & Roll : {self.roll}")


    @classmethod
    def instituteInfo(cls): # Class Method :- it is only access the static variable 
        print(f"Institute Name : {cls.InstituteName}")



s1 = Student("Yash",101)

s1.display()
s1.instituteInfo()
        