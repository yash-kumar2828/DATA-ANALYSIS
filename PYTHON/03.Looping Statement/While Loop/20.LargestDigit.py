# WAP to find out largest digit of a given number

num = int(input("Enter your number:"))
largest = 0

while num>0:
    lastDigit = num%10
    if lastDigit>largest:
        largest = lastDigit
    num = num//10


print(f"Largest digit is: {largest}")
