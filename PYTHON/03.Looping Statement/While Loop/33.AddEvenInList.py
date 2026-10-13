# WAP  to add all the even numbers present inside the given list.

l = eval(input("Enter your list:"))
sum = 0
i = 0

while i<len(l):
    if l[i]%2==0:
        sum = sum+l[i]
    i=i+1

print(f"Sum of all the even numbers present inside the list : {sum}")