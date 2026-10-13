# Check Whether a Number is an Automorphic Number

def is_automorphic_number(num):
    square = num**2
    rem = num%100
    return rem == num

num = int(input("Enter your number : "))

if is_automorphic_number(num):
    print(f"{num} is automorphic number")

else:
    print(f"{num} is not automorphic number")