class A():
    def car(self):
        print("Alto-800")


class B(A):
    def car(self):
        print('Scorpio')
        super().car()


b1 = B()

b1.car()
