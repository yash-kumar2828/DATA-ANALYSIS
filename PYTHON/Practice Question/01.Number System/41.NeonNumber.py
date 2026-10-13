# Check Whether a Number is a Neon Number
def get_square(n):
    return n**2

def get_digit_sum(n):
    sum = 0
    square = get_square(n)
    while square>0:
        rem = square%10
        sum = sum+rem
        square//=10
    return sum

def is_neon_number(n):
    sum = get_digit_sum(n)
    return n==sum

num = int(input("Enter your number : "))

if is_neon_number(num):
    print(f"{num} is neon number ")

else:
    print(f"{num} is not neon number ")