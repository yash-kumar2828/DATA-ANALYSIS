# Calculate the Power of a Number

def get_power(base,exponent):
    if exponent == 0:
        return 1

    return base*get_power(base,exponent-1)

base = int(input("Enter your base : "))
exponent = int(input("Enter your exponent : "))

res = get_power(base,exponent)
print(f"{base} to the power of {exponent} is : {res}")