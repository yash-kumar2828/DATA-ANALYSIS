# WAP to count how many factors we have for particular number.

num = int(input("Enter your number:"))
count = 0

for i in range(1,num+1):
    if num%i==0:
        count+=1

print(f"The total factor of {num} is : {count}")