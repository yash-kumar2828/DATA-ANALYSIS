# WAP to multiply all the odd numbers by taking range from the users

start = int(input("Enter your starting number:"))
end = int(input("Enter ypur ending number:"))
mul = 1

if start<end:
    while start<=end:
        if start%2!=0:
            mul=mul*start
        start=start+1

else:
    while start>=end:
        if start%2!=0:
            mul=mul*start
        start=start-1


print(f"Multiplication of odd numbers is : {mul}")
