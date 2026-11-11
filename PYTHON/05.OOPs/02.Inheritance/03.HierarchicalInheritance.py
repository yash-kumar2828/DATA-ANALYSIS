class A():
    def m1(self):
        print("This is m1 method")



class B(A):
    def m2(self):
        print("This is m2 method")



class C(A):
    def m3(self):
        print("This is m3 method")



c1 = C()
b1 = B()

c1.m1()
c1.m3()

b1.m1()
b1.m2()