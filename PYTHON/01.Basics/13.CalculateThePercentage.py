# WAP to calculate the percentage of a student marks.

M = int(input("Enter your marks of math:"))
H = int(input("Enter your marks of hindi:"))
S = int(input("Enter your marks of scince:"))
E = int(input("Enter your marks of english:"))
SS = int(input("Enter your marks of social science:"))

per = ((M+H+S+E+SS)/500)*100

print(f"The percentage of 5 subject is:{per}")
