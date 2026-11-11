class A():
    def __init__(self):
        print("First Constructor")


class B(A):
    def __init__(self):
        print("Second Constructor")


b1 = B()