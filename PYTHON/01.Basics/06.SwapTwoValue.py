# WAP to swap the value 

x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))

print(f"Before swapping the value of x and y are: {x} & {y}")

x,y = y,x

print(f"After swapping the value of x and y are: {x} & {y}")