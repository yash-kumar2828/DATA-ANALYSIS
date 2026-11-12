class Sample():

    def __init__(self,name):
        self.__name = name # Private Member (__) :- It is only access from the inside the class

    def display(self):
        print(f"My name is : {self.__name}")


s1 = Sample("Yash")

s1.display()


