# WAP to print the occurance of each and every charater 
# I/P :- ababca
# O/P :- a occured 3
#        b occured 2
#        c occured 1

str1 = input("Enter your string : ")
d = {}

for i in str1:
    d[i] = d.get(i,0)+1

for i in d:
    print(f"{i} occured {d[i]} times")