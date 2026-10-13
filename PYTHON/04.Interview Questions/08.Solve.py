# WAP to count the occurence of a given characters 
# I/P :- ababac
# O/P:- {'a':3,'b':2,'c':1}

str1 = input("Enter your string : ")
d = {}

for i in str1:
    d[i] = d.get(i,0)+1

print(d)