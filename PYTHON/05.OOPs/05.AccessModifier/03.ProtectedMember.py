class A():
    _x = 100 # Protectd Member
    def display(self):
        print(f"Value of x is : {self._x}")


class B(A):
    pass

b1 = B()
b1.display()
print(b1._x)


a1 = A()
a1.display()
print(a1._x)