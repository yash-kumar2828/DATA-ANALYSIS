# WAP to add all the elements which is present at the even index number and odd index number separately using for loop.

l1 = eval(input("Enter your list:"))
evenSum = 0
oddSum = 0

for i in range(0,len(l1)):
    if i%2==0:
        evenSum+=l1[i]

    else:
        oddSum+=l1[i]

print(f"Add all the even index element present inside list : {evenSum}")
print(f"Add all the odd index element present inside list : {oddSum} ")

