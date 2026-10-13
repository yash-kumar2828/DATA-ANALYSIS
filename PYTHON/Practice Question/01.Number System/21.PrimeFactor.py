# Find the Prime Factors of a Number

num = int(input("Enter your number : "))

for i in range(2,num+1):
    count = 0
    for j in range(1,i+1):
        if i%j==0:
            count = count+1
    if count == 2:
        if num%i==0:
            print(i,end=" ")
    