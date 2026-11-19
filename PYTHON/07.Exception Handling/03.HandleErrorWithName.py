try:
    x = int(input("Enter the value of x : "))
    y = int(input("Enter the value of y : "))
    res = x/y
    print(f"Division is : {res}")

except ValueError:
    print("Please provide only integer value")

except ZeroDivisionError:
    print("Please don't provide the second value as 0")


except Exception as e:
    print(e)
    