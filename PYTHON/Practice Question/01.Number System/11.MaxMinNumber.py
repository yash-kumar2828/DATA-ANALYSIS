# Find the Maximum and Minimum Digit in a Number

num = int(input("Enter your positive number : "))
max = num%10
min = num%10

while num>0:
    lastDigit = num%10
    if lastDigit>max:
        max = lastDigit

    if lastDigit<min :
        min = lastDigit

    num = num//10

print(f"{max} is a maximum digit")
print(f"{min} is a minimum digit")