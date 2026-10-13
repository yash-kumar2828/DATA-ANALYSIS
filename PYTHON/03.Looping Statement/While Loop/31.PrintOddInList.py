# WAP to print all the odd number which is present inside the list.

l = eval(input("Enter your list:"))
i =0

print("Print all the odd number which is present inside the list:")
while i<len(l):
    if l[i]%2!=0:
        print(l[i])
    i+=1