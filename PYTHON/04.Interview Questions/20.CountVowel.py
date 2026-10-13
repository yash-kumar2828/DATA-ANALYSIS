# WAP to count the occurance of each vowel present inside the given string

s = input("Enter your string : ")
d = {}

for i in s:
    if i in 'AEIOUaeiou':
        d[i]=d.get(i,0)+1

print(d)