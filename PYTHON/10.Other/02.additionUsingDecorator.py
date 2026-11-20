def decorAdd(func):
    def inner(n1,n2):
        print(f"{'*'*20}")
        func(n1,n2)
        print(f"{'*'*20}")
    return inner

@decorAdd
def add(n1,n2):
    print(f"Addition is : {n1+n2}")

add(10,20)