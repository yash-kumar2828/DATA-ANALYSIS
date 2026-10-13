# WAP to take a dictionary as input and display each key of a dictionary line by line.

d = eval(input("Enter your dictionary:"))

for i in d:
    print(i)




# WAP to take a dictionary as input and display each values of a dictionary line by line.

d2 = eval(input("Enter your dictionary:"))

for i in d2.values():
    print(i)



# WAP to take a dictionary as input and display each values and keys of a dictionary line by line.

d3 = eval(input("Enter your dictionary:"))

for i in d3.items():
    print(i)