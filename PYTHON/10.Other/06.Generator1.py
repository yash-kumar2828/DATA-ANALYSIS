def generator1():
    yield 10
    yield 20
    yield 30


g = generator1()
print(next(g))
print(next(g))
print(next(g))