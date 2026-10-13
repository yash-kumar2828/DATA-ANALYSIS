# WAP to take a tuple as an input and multiply those elements which are present at odd index number.

t1 = eval(input("Enter your tuple:"))
mul = 1
i = 0

while i<len(t1):
    if i%2!=0:
        mul=mul*t1[i]
    i=i+1

print(f"Multiply those element which are present at odd index number : {mul}")