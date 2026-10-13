# Check Whether a Number is a Harshad Number

def is_harshad_number(num):
    sum = 0
    temp = num
    while num>0:
        rem = num%10
        sum = sum+rem
        num//=10
    return temp%sum==0

num = int(input("Enter your number : "))

if is_harshad_number(num):
    print(f"{num} is harshad number ")

else:
    print(f"{num} is not harshad number")