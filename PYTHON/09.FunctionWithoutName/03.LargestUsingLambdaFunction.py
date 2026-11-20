# WAP to find the largest among three numbers using lambda function

largest = lambda n1,n2,n3 : n1 if n1>n2 and n1>n3 else n2 if n2>n3 else n3

print(f"Largest number is : {largest(11,21,9)}")