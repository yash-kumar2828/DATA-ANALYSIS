class Sample():

    def __init__(self,name):
        self.name = name  # Public Member :- It is access from inside the class as well as from outside the class

    def display(self):
        print(f"My name is : {self.name}")


s1 = Sample("Yash")

s1.display()

print(s1.name)

    