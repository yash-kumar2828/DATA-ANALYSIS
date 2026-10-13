# WAP to display all factors of a given number.
num = int(input("Enter your number:"))

print(f"All factors of {num}:")
for i in range(1,num+1):
    if num%i==0:
        print(i,end=" ")