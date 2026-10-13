# Check Whether a Number is Perfect, Abundant, or Deficient

def is_perfect_number(num):
    sum = 0
    for i in range(1,num//2+1):
        if num%i==0:
            sum+=i

    return sum == num

def is_abundant_number(num):
    sum = 0
    for i in range(1,num//2+1):
        if num%i==0:
            sum+=i
    return sum>num

def is_deficient_number(num):
    sum = 0
    for i in range(1,num//2+1):
        if num%i==0:
            sum+=i

    return sum<num

num = int(input("Enter your number : "))

if num<=0:
    print("Please enter the positive number")
elif is_perfect_number(num):
    print(f"{num} is perfect number")

elif is_abundant_number(num):
    print(f"{num} is abundant number")

elif is_deficient_number(num):
    print(f"{num} is deficient number")