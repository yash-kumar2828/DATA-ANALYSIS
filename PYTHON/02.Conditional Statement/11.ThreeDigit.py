# WAP to check wheather a given number is 3 digit or not

num = int(input("Enter your number:"))

if num>=100 and num<=999:
    print(f"{num} is three digit number")

else:
    print(f"{num} is not three digit number")