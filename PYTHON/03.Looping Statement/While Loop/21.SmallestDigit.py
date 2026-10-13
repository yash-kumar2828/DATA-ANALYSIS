# WAP  to find the smallest digit of present inside the given number

num = int(input("Enter your number:"))
small = 9

while num>0:
    lastDigit = num%10
    if lastDigit<small:
        small = lastDigit
    num = num//10

print(f"Smallest digit is :{small}")