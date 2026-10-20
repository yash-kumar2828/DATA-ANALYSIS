# Calculate Permutations: N People Occupying R Seats
# Formula :-  nPr = n!/(n-r)!

def get_permutations(n,r):
    perm = 1

    for i in range(r):
        perm = perm*(n-i)

    return perm
    

n = int(input("Enter the value of n : "))
r = int(input("Enter the value of r : "))

res = get_permutations(n,r)
print(f"The permutations is : {res}")
