# WAP to reverse each word of a given string :-
# I/P :- python is easy to learn
# O/P :- nohtyp si ysae ot nrael

str1 = input("Enter your string : ")
l = str1.split()
res = []

for i in l:
    res.append(i[::-1])

output = " ".join(res)
print(output)