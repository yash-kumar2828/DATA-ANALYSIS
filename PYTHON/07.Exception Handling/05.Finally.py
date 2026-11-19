try:
    x = int(input("Enter the value of x : "))
    y = int(input("Enter the value of y : "))
    res = x/y
    print(f"Division is : {res}")


except Exception as e:
    print(e)


finally:
    print("Always work")