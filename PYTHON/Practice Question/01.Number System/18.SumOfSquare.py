# Find the Sum of Squares of Digits

num = int(input("Enter your number : "))
digit_sum = 0

while num>0:
    rem = num%10
    digit_sum = digit_sum + (rem**2)
    num = num//10

print(f"Sum of square of digits is : {digit_sum}")