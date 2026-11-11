class Employee():

    def __init__(self,ename,eid):  # __init__ is a constructor
        self.ename = ename  # Instance Variable
        self.eid = eid      # Instance Variable


    def display(self): # if first argument is self then it is called instance method and it can only access the instance variable
        print(f"EmpName : {self.ename} & EmpId : {self.eid}")


e1 = Employee("Yash",'E101')
e1.display()