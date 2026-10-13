# WAP to count the occurance of each consonant present inside the given string

s = input("Enter your string : ")
d = {}

for i in s:
    if i.isalpha() and i not in 'AEIOUaeiou':
        d[i]=d.get(i,0)+1

print(d)