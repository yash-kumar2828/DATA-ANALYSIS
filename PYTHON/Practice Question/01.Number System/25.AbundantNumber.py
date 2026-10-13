# Check Whether a Number is an Abundant Number

def is_abundant_number(num):
    sum = 0
    for i in range(1,num//2+1):
        if num%i==0:
            sum+=i

    return sum>num

num = int(input("Enter your number : "))

if is_abundant_number(num):
    print(f"{num} is abundant number ")
else:
    print(f"{num} is not abundant number")
    

