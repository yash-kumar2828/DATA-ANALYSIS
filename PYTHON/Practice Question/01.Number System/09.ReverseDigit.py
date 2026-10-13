# Reverse the Digits of a Number 

num = int(input("Enter your positive number : "))
rev = 0

while num>0:
    rem = num%10
    rev = rev*10+rem
    num = num//10

print(f"Reverse the digits of a number is : {rev}")