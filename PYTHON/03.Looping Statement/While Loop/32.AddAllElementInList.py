# WAP to take a list as input and add all the element present inside the list.

l = eval(input("Enter your list:"))
sum = 0
i = 0

while i<len(l):
    sum=sum+l[i]
    i=i+1

print(f"The sum of list is:{sum}")