def generator3():
    for i in range(1,11):
        yield i


g = generator3()

for i in g:
    print(i,end=" ")