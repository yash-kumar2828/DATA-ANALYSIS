def decoratorWish(func):
    def inner(name):
        print(f"{'*'*20}")
        print(f"Best of luck : {name}")
        print(f"{'*'*20}")

    return inner

@decoratorWish
def wish(name):
    print(f"Good Morning : {name}")


wish("Yash")