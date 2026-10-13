# WAP to create a calculator to perform operation like +, -, *, /, //, **, %

num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))
symbol = input("Enter the symbol to perform operations like +, -, *, /, //, **, %  :")

if symbol=='+':
    print(f"addition of {num1} & {num2} is: {num1+num2}")

elif symbol=='-':
    print(f"subtraction of {num1} & {num2} is: {num1-num2}")

elif symbol=='*':
    print(f"multiplication of {num1} & {num2} is: {num1*num2}")

elif symbol=='/':
    if num2==0:
        print(f"{num2} is invalid input")
    else:
        print(f"division of {num1} & {num2} is: {num1/num2}")

elif symbol=='//':
    if num2==0:
            print(f"{num2} is invalid input")
    else:
        print(f"Floor division of {num1} & {num2} is: {num1// num2}")

elif symbol=='**':
    print(f"{num1} to the power {num2} is: {num1**num2}")

elif symbol=='%':
    print(f"modulus of {num1} & {num2} is: {num1%num2}")

else:
    print("your choice is invalid")