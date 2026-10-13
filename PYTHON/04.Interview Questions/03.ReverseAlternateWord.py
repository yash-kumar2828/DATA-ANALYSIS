# WAP to reverse every alternate word of a given string.
# I/P :-my name is yash kumar
# O/P :-my eman is hsay kumar

str1 = input("Enter your string : ")
l = str1.split()
res = []
i = 0

while i<len(l):
    if i%2==0:
        res.append(l[i])
    else:
        res.append(l[i][::-1])
    i=i+1    

output = " ".join(res)
print(output)