# Check Whether a Number is a Happy Number

def is_happy_number(n):
    while n>9:
        sum = 0
        while n>0:
            rem = n%10
            sum = sum+rem**2
            n//=10
        n=sum
    return n==1

num = int(input("Enter your number : "))

if is_happy_number(num):
    print(f"{num} is happy number ")

else:
    print(f"{num} is not happy number ")
    

        