# WAP  to determine the age group of a person based on the given below table:- 60-above -> senior citizen, 20-59 -> adult, 12-19 -> Teenage, Below 12 -> child

age = float(input("Enter your age in year:"))

if age>=60:
    print("You are sinior citizen")

elif age>=20 and age<60 :
    print("You are adult")

elif age>=12 and age<20:
    print("You are teenage")

else:
    print("You are child")