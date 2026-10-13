# Check Whether a Number is a Duck Number

def is_duck_number(n):
    if n<=0:
        return False
    has_zero = False
    while n>0:
        rem = n%10
        if rem == 0:
            has_zero = True
            break
        n//=10
    return has_zero

num = int(input("Enter your number : "))
if is_duck_number(num):
    print(f"{num} is duck number")
else:
    print(f"{num} is not duck number")
