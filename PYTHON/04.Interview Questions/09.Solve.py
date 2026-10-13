# WAP to find the occurence of each word 
# I/P :- Yash Kumar Kumar Yash Singh
# O/p :- {'Yash':2,'Kumar':2,'Singh':1}

str1 = input("Enter your string : ")
l = str1.split()
d = {}

for i in l:
    d[i] = d.get(i,0)+1

print(d)