# WAP to solve the given below:-
# I/P :- a4b3c4
# O/P :- aaaabbbcccc

str1 = input("Enter your string : ")
res = ""

for i in str1:
    if i.isalpha():
        alpha = i
    else:
        num = int(i)
        res = res+(alpha*num)

print(res)

