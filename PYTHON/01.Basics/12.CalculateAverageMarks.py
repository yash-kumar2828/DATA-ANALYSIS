# WAP to take the marks of a student and calculate the average marks of the student

M = int(input("Enter your marks of math:"))
H = int(input("Enter your marks of hindi:"))
S = int(input("Enter your marks of scince:"))
E = int(input("Enter your marks of english:"))
SS = int(input("Enter your marks of social science:"))

avg = (M+H+S+E+SS)/5

print(f"The average of 5 subject is:{avg}")
