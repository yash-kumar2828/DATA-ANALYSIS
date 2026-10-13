# WAP to add all the digit that is present inside the given number

num = int(input("Enter your number:"))
sum = 0

while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10

print(f"The sum of all digit present inside the given number is: {sum}")