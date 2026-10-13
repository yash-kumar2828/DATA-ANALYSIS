# Find the LCM of Two Numbers

def get_gcd(a,b):
    if a==0:
        return b
    return get_gcd(b%a,a)

def get_lcm(n1,n2):
    gcd = get_gcd(n1,n2)
    return (n1*n2)//gcd

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
res = get_lcm(num1,num2)

print(f"LCM of two number is : {res}")