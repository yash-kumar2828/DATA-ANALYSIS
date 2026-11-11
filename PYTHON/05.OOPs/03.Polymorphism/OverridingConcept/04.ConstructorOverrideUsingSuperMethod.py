class A():
    def __init__(self):
        print("Hello World")


class B(A):
    def __init__(self):
        super().__init__()
        print("Hello Universe")


b1 = B()