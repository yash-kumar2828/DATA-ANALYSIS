# Calculate Combinations: Select R People from N People
# Formula:- nCr = n!/(r! * (n-r)!)

def get_combination(n,r):
    comb = 1

    for i in range(r):
        comb = comb * (n-i)//(i+1)

    return comb

n = int(input("Enter the value of n : "))
r = int(input("Enter the value of r : "))

res = get_combination(n,r)
print(f"The combinations is : {res}")
