# Count the Number of Digits in an Integer 

num = int(input("Enter your positive number : "))
count = 0

while num>0:
    count+=1
    num=num//10

print(f"number of digit is : {count}")
