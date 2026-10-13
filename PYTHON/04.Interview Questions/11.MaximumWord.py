# WAP to print the word which appears maximum number of time inside a sentence
# I/P :- Yash Kumar Yash Kumar Yash Singh
# O/P :- Yash

str1 = input("Enter your string : ")
l = str1.split()
d ={}

for i in l:
    d[i] = d.get(i,0)+1

res = []
for i in d:
    res.append(d[i])

res.sort()
largest = res[-1]

for i in d:
    if largest == d[i]:
        print(i)
        break
