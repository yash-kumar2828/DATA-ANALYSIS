# Find the Sum of Digits of a Number 

num = int(input("Enter your positive number : "))
sum = 0

while num>0:
    rem = num%10
    sum =sum+rem
    num = num//10

print(f"Sum of digit is : {sum}")