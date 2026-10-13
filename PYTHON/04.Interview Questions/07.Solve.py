# WAP to solve the given below requirement :-
# I/P :- b2c4a4
# O/P :- aaaabbcccc

str1 = input("Enter your string : ")
res = ""

for i in str1:
    if i.isalpha():
        alpha = i
    else:
        num = int(i)
        res = res+(alpha*num)

output = "".join(sorted(res))
print(output)