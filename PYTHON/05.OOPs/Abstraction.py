from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def loan(self):
        pass

    def detail(self):
        print("Loan is paid")



class B(A):
    def loan(self):
        print("Home loan is paid")  

b = B()
b.loan()
b.detail()
