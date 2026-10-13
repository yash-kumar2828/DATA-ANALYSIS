# WAP to check wheather a given number is even or odd, if it is even then square the number and if it odd then cube the number

num = int(input("Enter your number:"))

if num%2==0:
    print(f"The square of {num} is: {num**2}")

else:
    print(f"The cube of {num} is: {num**3}")