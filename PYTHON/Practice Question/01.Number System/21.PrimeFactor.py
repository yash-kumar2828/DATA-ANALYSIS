# Find the Prime Factors of a Number

num = int(input("Enter your number : "))

i = 2

while i<=num:
    while num%i == 0:
        print(i,end=" ")
        num//=i

    i=i+1