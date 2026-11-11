class Book():

    def __init__(self,x):
        self.page = x

    def __add__(self, other):   # Magic method :- in magic method two argument first is self and second is other and they are fixed 
        return self.page + other.page


b1 = Book(200)
b2 = Book(300)

print(b1+b2)