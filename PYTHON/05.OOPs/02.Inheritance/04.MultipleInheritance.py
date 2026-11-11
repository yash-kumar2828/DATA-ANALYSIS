class A():
    def m1(self):
        print("This is m1 method")


class B():
    def m2(self):
        print("This is m2 method")


class C():
    def m3(self):
        print("This is m3 method")


class D(A,B,C):
    def m4(self):
        print("This is m4 method")


d1 = D()

d1.m1()
d1.m2()
d1.m3()
d1.m4()