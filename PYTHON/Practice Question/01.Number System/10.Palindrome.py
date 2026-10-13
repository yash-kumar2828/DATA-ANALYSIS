# Check Whether a Number is a Palindrome

num = int(input("Enter your positive number : "))
temp = num
rev = 0

while num>0:
    rem = num%10
    rev = rev*10+rem
    num = num//10

if temp == rev:
    print(f"{temp} is a palindrome number")

else:
    print(f"{temp} is not a palindrome number")