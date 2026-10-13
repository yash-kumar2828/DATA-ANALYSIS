# Count the Occurrences of a Given Digit 

num = int(input("Enter your positive number : "))
digit = int(input("Enter your digit you want to count : "))
count = 0

while num>0:
    rem = num%10
    if digit == rem:
        count+=1
    num = num//10

print(f"The digit of {digit} is {count} time occur")

