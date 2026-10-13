# Calculate Combinations: Select R People from N People
# Formula:- nCr = n!/(r! * (n-r)!)

def get_factorial(n):
    if n == 0 or n==1:
        return 1

    return n*get_factorial(n-1)

def get_combination(n,r):
    a = get_factorial(n)
    b = get_factorial(r)
    c = get_factorial(n-r)

    return a//(b*c)

n = int(input("Enter the value of n : "))
r = int(input("Enter the value of r : "))

res = get_combination(n,r)
print(f"The combinations is : {res}")
