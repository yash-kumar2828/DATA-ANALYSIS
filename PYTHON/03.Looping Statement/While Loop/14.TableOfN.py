# WAP  to print the table by taking input from user

table = int(input("Enter your number : "))
i = 1

print(f"The table of {table}:")
while i<=10:
    print(f"{table} * {i} = {table*i}")
    i=i+1