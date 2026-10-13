# Check Whether a Number is a Perfect Number

def is_perfect_number(n):
    sum = 0
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i

    return n==sum

num = int(input("Enter your number : "))
if is_perfect_number(num):
    print(f"{num} is perfect number ")
else:
    print(f"{num} is not perfect number")
    