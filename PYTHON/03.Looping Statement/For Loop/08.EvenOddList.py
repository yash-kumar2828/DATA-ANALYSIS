# WAP  to add all the even element as well as multiply all the odd element separately from the given list.

l1 = eval(input("Enter your list:"))
evenSum = 0
oddMultiply = 1

for i in l1:
    if i%2==0:
        evenSum+=i
    else:
        oddMultiply*=i

print(f"Add all the even element present inside list is : {evenSum}")
print(f"Multiply all the odd element present inside list is : {oddMultiply}")