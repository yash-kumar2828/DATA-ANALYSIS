# WAP  to add those element only which are present at even index number inside the list.

l = eval(input("Enter your list:"))
sum =0
i =0

while i<len(l):
    if i%2==0:
        sum =sum+l[i]
    i=i+1

print(f"sum of even index number is :{sum}")