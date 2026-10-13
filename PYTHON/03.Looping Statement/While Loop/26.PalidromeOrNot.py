# WAP to check  wheather a given number is palidrome or not using while loop

num = int(input("Enter your number:"))
temp = num
rev = 0

while num>0:
    rem = num%10
    rev = rev*10+rem
    num = num//10


if temp==rev:
    print(f"{temp} is a palidrome number")

else:
    print(f"{temp} is not a palidrome number")