# WAP to check whether a given number is perfect number or not.

num = int(input("Enter your number:"))
sum = 0

for i in range(1,num):
    if num%i==0:
        sum+=i

if num==sum:
    print(f"{num} is a perfect number")

else:
    print(f"{num} is not a perfect number")