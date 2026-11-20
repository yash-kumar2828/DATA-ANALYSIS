def generator2():
    yield 10
    yield 20
    yield 30

g = generator2()

for i in g:
    print(i)