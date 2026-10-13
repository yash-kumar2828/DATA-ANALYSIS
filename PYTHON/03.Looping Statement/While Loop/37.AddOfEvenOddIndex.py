# WAP to take a list as input and add all the elements which are present at even index number as well as odd index number separately.

l1 = eval(input("Enter your list:"))
evenSum = 0
oddSum = 0
i = 0

while i<len(l1):
    if i%2==0:
        evenSum=evenSum+l1[i]
    else:
        i%2!=0
        oddSum=oddSum+l1[i]
    i=i+1

print(f"Add all even index present inside list is : {evenSum}")
print(f"Add all odd index present inside list is : {oddSum}")