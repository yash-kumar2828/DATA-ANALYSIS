# Find the Product of Digits of a Number 

num = int(input("Enter your number : "))
mul = 1

while num>0:
    rem = num%10
    mul = mul*rem
    num = num//10

print(f"Product of digit of a number is : {mul}")

