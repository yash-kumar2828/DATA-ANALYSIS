# WAP to print the fibonacci series up to a given length.
                        # OR 
# WAP to print the fibonacci series.

num = int(input("Enter your number:"))
a = 0
b = 1

print(a,b,end=" ")
for i in range(num-2):
    c = a+b
    print(c,end=" ")
    a = b
    b = c