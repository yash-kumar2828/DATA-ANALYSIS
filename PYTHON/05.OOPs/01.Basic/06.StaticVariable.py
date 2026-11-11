class Student():

    InstituteName = 'QSpider'

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name : {self.name}, Roll : {self.roll}, & Institute Name : {self.InstituteName}")


s1 = Student("Yash",101)
s2 = Student("Kumar",102)

s1.display()
s2.display()
        