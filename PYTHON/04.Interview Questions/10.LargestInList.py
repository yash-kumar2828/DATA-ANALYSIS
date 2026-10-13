# WAP to take a list as input and find the largest element present inside the list

l = eval(input("Enter your list : "))

largest = 0

for i in l:
    if i>largest:
        largest = i

print(f"{largest} is a largest element present inside the list")