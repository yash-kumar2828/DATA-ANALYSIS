# Check Whether a Number is an Armstrong Number

def count_digit(num):
    count = 0
    while num>0:
        count+=1
        num//=10
    return count

def is_armstrong(num):
    count = count_digit(num)
    res = 0
    temp = num
    while num>0:
        rem = num%10
        res = res+(rem**count)
        num//=10
    return temp == res



num = int(input("Enter your number : "))

if is_armstrong(num):
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not armstrong number")