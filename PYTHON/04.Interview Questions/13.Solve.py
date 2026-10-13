# WAP to solve the given below requirement 
# I/P :- 3b2c4a
# O/P :- aaaabbbcc

str1 = input("Enter your string : ")
res = ""

for i in str1:
    if i.isdigit():
        num = int(i)
    else:
        alpha = i
        res = res+(alpha*num)

output = "".join(sorted(res))
print(output)

