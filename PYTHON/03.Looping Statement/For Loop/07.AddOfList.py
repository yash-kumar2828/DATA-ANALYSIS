# WAP to take a list as input and add all the element present inside the given list.

l1 = eval(input("Enter your list:"))
sum = 0

for i in l1:
    sum+=i

print(f"Add all the element present inside list : {sum}")