# Find the Sum of First N Natural Numbers

num = int(input("Enter your positive number : "))
sum = 0
i = 0
while i<=num:
    sum = sum+i
    i = i+1

print(f"Sum of n natural numbers are : {sum}") 