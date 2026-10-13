# WAP that print string with all commas replace by (.)

s = input("Enter your string : ")
res = ""

for i in s:
    if i==",":
        i = "."
        res = res+i
    else:
        res = res+i

print(res)