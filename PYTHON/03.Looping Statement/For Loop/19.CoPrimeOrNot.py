# WAP to check whether the given numbers are Co-Prime to each other or not.

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))

if num1<num2:
    small = num1

else:
    small = num2

for i in range(1,small+1):
    if num1%i==0 and num2%i==0:
        hcf = i

if hcf == 1:
    print("Numbers are Co-Prime to each other")

else:
    print("Numbers are not Co-Prime to each other")