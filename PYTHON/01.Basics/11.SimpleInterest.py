# WAP to calculate the simple interest for a given principal amount, rate of interest and time period

p = int(input("Enter a principal amount:"))
r = float(input("Enter a rate of interest:"))
t = float(input("Enter a time period in year:"))

SI = (p*r*t)/100

print(f"Simple interest of {p} is: {SI}")