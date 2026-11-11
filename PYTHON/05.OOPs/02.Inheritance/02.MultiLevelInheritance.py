class A():
    def car(self):
        print("Alto")


class B(A):
    def bike(self):
        print("Splender")


class C(B):
    def cycle(self):
        print("Cycle")


c1 = C()
c1.car()
c1.bike()
c1.cycle()
