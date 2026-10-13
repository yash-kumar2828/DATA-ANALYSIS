# Repeatedly Add Digits Until a Single Digit Remains 

num = int(input("Enter your number : "))

while num>9:
    sum = 0
    while num>0:
        rem = num%10
        sum = sum+rem
        num = num//10
    num = sum    

print(f"Repeatedly add digit until a single digit : {num}")
