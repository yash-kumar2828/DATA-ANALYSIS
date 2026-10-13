# Check Whether Two Numbers are Co-Prime

def get_gcd(a,b):
    if a==0:
        return b
    return get_gcd(b%a,a)

def is_co_prime(n1,n2):
    gcd = get_gcd(n1,n2)
    return gcd == 1

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
if is_co_prime(num1,num2):
    print("It is Co-Prime")

else:
    print("It is not Co-Prime")