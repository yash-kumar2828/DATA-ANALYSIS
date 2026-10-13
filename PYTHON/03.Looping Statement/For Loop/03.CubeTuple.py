# WAP to take a tuple as input and cube all the element present inside the given tuple.

t1 = eval(input("Enter your tuple:"))

print("Cube all the element present inside the given tuple:")
for i in t1:
    print(i**3,end=" ")