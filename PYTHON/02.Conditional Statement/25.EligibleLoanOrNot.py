# WAP to check wheather a person is eligible for loan or not based on the given below condition:- i). Age should be above 21 and ii).salary should be 30000 

age = int(input("Enter your age:"))
sal = int(input("Enter your salary:"))

if age>21:
    if sal>=30000:
        print("You are eligible for loan")

    else:
        print("You are not eligibe for loan")

else:
    print("You are not eligible for loan")
