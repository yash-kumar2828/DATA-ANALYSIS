# Find the Roots of a Quadratic Equation
# Formula:- d = b**2 - 4ac
#           root:- (-b+d**0.5)/2*a ,  (-b-d**0.5)/2*a

def find_roots(a,b,c):
    d = b**2-4*a*c

    if d>0:
        sqr_root_of_d = d**0.5
        root1 = (-b+sqr_root_of_d)/2*a
        root2 = (-b-sqr_root_of_d)/2*a

        if root1 == int(root1):
            root1 = int(root1)

        if root2 == int(root2):
            root2 = int(root2)

        print(f"Real and different roots : {root1}, {root2}")

    elif d == 0:
        root = -b/(2*a)
        if root == int(root):
            root = int(root)
        print(f"Real and equal roots : {root}")

    else:
        print("Complex")


a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

if a == 0:
    print("The value of a = 0 is don't possible")
else:
    find_roots(a,b,c)