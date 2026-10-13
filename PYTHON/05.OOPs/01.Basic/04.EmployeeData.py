# WAP to create employee class to store the employees name, employee salary, id card number

class Employee:
    def __init__(self,name,salary,id):
        self.name = name
        self.salary = salary
        self.id = id

    def display(self):
        print(f"Employee Data :- ")
        print(f"Name : {self.name}")
        print(f"Salary : {self.salary}")
        print(f"ID : {self.id}")

emp1 = Employee("Yash",45000,101)
emp2 = Employee("Kumar",50000,102)

emp1.display()
emp2.display()
        