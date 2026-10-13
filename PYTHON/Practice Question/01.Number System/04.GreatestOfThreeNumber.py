# Find the Greatest of Three Numbers

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
num3 = int(input("Enter youe third number : "))


if num1==num2==num3:
    print("All values are equal")
    
elif num1>num2 and num1>num3:
    print(f"{num1} is a greatest number")

elif num2>num3:
    print(f"{num2} is a greatest number")

else:
    print(f"{num3} is a greatest number")
