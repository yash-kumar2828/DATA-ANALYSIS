# WAP to take a student percentage as input and determine following grade based on given below table:- 90 and above -> A, 75-89 -> B, 60-74 -> C, 40 - 59 -> D, Below 40 -> Fail
 

per = float(input("Enter your percentage: "))

if per>=90 and per<=100:
    print("Grade A")

elif per>=75 and per<90:
    print("Grade B")

elif per>=60 and per<75:
    print("Grade C")

elif per>=40 and per<60:
    print("Grade D")

elif per>=1 and per<40:
    print("Fail")

else: 
    print("Invalid percentage")

