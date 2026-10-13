# WAP to count the number of digit present inside the given number using while loop

num = int(input("Enter your number:"))
count = 0

while num>0:
    count = count+1
    num =num//10

print(f"It is a {count} digit number")
