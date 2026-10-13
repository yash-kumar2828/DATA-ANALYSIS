# WAP to take a tuple as input and multiply all the element present inside the tuple.

t1 = eval(input("Enter your tuple:"))
mul = 1
i = 0

while i<len(t1):
    mul = mul*t1[i]
    i=i+1

print(f"Multiply all the element present inside the tuple is :{mul}")
