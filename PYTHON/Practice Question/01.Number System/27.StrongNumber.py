# Check Whether a Number is a Strong Number
def get_factorial(n):
    if n==1:
        return 1
    return n*get_factorial(n-1)

def is_strong_number(num):
    sum = 0
    temp = num
    while num>0:
        rem = num%10
        sum = sum+get_factorial(rem)
        num//=10
    return temp == sum

num = int(input("Enter your number : "))

if is_strong_number(num):
    print(f"{num} is strong number")

else:
    print(f"{num} is not perfect number")