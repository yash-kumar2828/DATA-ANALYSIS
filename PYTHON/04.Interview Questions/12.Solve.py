# WAP to solve the given below requirement 
# I/P :-  aaaabbbccc
# O/P :- 4a3b3c

str1 = input("Enter your string : ")
d = {}

for i in str1:
    d[i] = d.get(i,0)+1

res = ""
for i in d:
    res = res+str(d[i])+i

print(res)
