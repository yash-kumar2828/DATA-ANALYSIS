class A():
    def m1(self):
        print("This is m1 method")


class B(A):
    def m2(self):
        print("This is m2 method")


class C(B):
    def m3(self):
        print("This is m3 method")


class D(B):
    def m4(self):
        print("This is m4 method")


d1 = D()
c1 = C()

d1.m1()
d1.m2()
d1.m4()

c1.m1()
c1.m2()
c1.m3()