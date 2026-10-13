# WAP to multiplication of all the digit that is present inside the given number

num = int(input("Enter your number:"))
mul = 1

while num>0:
    rem=num%10
    mul=mul*rem
    num=num//10

print(f"The multiplication of all digit present inside the given number is: {mul}")