# Find the Factorial of a Number

def get_factorial(num):
    if num == 0 or num == 1:
        return 1
    return num*get_factorial(num-1)

num = int(input("Enter your number : "))
res = get_factorial(num)

print(f"Factorial of {num} is : {res}")