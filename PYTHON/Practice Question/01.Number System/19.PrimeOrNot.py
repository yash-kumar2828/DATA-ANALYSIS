# Check Whether a Number is Prime

num = int(input("Enter your number : "))

count = 0
if num<=1:
    print(f"{num} is not prime number")

else:
    for i  in range(2,int(num**0.5)+1):
        if num%i==0:
            count = count+1
            break

    if count == 0:
        print(f"{num} is prime number")

    else:
        print(f"{num} is not prime number")
            

