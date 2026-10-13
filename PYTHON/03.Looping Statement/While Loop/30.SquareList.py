# WAP to take a list as input and square all the element of given list.
l = eval(input("Enter your list:"))
i = 0

print("The square of given list:")
while i<len(l):
    sqr=l[i]**2
    print(sqr)
    i=i+1

