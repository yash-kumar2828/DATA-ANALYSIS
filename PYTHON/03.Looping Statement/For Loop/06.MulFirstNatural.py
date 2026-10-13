# WAP  to multiply first n natural number.

num =int(input("Enter your number:"))
mul = 1

for i in range(1,num+1):
    mul*=i

print(f"multiply of first n natural numbers are: {mul}")