# WAP to check wheather a person is eligible for bonus or not based on the given condition:- i). if year of experiance is greater than 5 and salary is above 50000 then bonus is 10000 otherwise if year of experiance more than 5 and salary is above 25000 then bonus is 5000 else no bonus

exp = float(input("Enter your experiance in year:")) 
sal = int(input("Enter your salary:"))

if exp>5:
    if sal>50000:
        bonus = 10000
        print(f"You are eligible for bonus and your bonus is : {bonus}")

    elif sal>25000:
        bonus = 5000
        print(f"You are eligible for bonus and your bonus is : {bonus}")

    else:
        print("You are not eligible for bonus")

else:
    print("You are not eligible for bonus")