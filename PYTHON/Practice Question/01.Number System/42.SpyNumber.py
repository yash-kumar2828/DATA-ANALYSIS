# Check Whether a Number is a Spy Number

def get_sum_of_digit(n):
    sum = 0
    while n>0:
        rem = n%10
        sum = sum+rem
        n//=10
    return sum

def get_product_of_digit(n):
    product = 1
    while n>0:
        rem = n%10
        product = product*rem
        n//=10
    return product

def is_spy_number(n):
    if n<=0:
        return False
    sum = get_sum_of_digit(n)
    product = get_product_of_digit(n)
    return sum == product

num = int(input("Enter your number : "))
if is_spy_number(num):
    print(f"{num} is spy number")
else:
    print(f"{num} is not spy number")