# WAP to check wheather a given number is divisible by both 3 & 5 if it is divisible by both then print number is divisible by both
num = int(input("Enter your number:"))

if num%3==0 and num%5==0:
    print(f"{num} is divisible by both 3 and 5") 