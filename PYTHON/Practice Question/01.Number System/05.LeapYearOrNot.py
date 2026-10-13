# Check Whether a Year is a Leap Year 

year = int(input("Enter your year : "))

if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a leap year")

else:
    print(f"{year} is a not a leap year")