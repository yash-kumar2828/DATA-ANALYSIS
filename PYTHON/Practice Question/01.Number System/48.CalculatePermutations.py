# Calculate Permutations: N People Occupying R Seats
# Formula :-  nPr = n!/(n-r)!


def get_factorial(n):
    if n==0 or n==1:
        return 1

    return n * get_factorial(n-1)

def get_permutations(n,r):
    a = get_factorial(n)
    b = get_factorial(n-r)
    return a//b
    

n = int(input("Enter the value of n : "))
r = int(input("Enter the value of r : "))

res = get_permutations(n,r)
print(f"The permutations is : {res}")
