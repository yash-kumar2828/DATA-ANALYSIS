# WAP to swap the value 

x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))

print(f"Before swapping the value of x and y are: {x} & {y}")

temp = x
x = y
y = temp

print(f"After swapping the value of x and y are: {x} & {y}")