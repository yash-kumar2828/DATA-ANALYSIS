# Add Two Fractions and Simplify the Result

def get_gcd(a,b):
    if a == 0:
        return b
    return get_gcd(b%a,a)


def get_add_two_fractions(numerator1, denominator1, numerator2, denominator2):
    numerator = (numerator1*denominator2)+(numerator2*denominator1)

    denominator = denominator1*denominator2
    x=numerator
    y=denominator
    gcd = get_gcd(x,y)

    print(f"Numerator : {x//gcd}, Denominator : {y//gcd}")


numerator1 = int(input("Enter the first numerator : "))
denominator1 = int(input("Enter the first denominator : "))
numerator2 = int(input("Enter the second numerator : "))
denominator2 = int(input("Enter the second denominator : "))

get_add_two_fractions(numerator1,denominator1,numerator2,denominator2)
