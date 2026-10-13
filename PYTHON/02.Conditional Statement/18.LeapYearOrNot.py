# WAP to check wheather a given year is leap year or not

year = int(input("Enter your year:"))

if year%4==0 and year%100!=0:
    print(f"{year} is a leap year")

elif year%400==0:
    print(f"{year} is a leap year")

else:
    print(f"{year} is not a leap year")