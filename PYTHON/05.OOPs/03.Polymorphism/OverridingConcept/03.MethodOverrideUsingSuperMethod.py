class A():
    def car(self):
        print("Alto-800")


class B(A):
    def car(self):
        print('Scorpio')

    def car2(self):
        super().car()


b1 = B()

b1.car()
b1.car2()