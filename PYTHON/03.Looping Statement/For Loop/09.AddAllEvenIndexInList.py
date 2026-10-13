# WAP to add all the elements which are present even index number inside a list.

l1 = eval(input("Enter your list:"))
sum = 0

for i in range(0,len(l1)):
    if i%2==0:
        sum+=l1[i]

print(f"Add all the even index element inside the list : {sum}")