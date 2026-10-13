# Remove a Given Digit from a Number 

num = int(input("Enter your number : "))
digit = int(input("Enter your digit do you want to delete : "))
place = 1
number = 0
while num>0:
    rem = num%10
    if digit!=rem:
        number =number+rem*place
        place*=10
    num//=10

print("The number is : ",number)




