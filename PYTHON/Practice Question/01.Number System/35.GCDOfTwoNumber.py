# Find the GCD of Two Numbers

def get_gcd(a,b):
    if a==0:
        return b
    return get_gcd(b%a,a)

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
res = get_gcd(num1,num2)

print(f"GCD of two number is : {res}")