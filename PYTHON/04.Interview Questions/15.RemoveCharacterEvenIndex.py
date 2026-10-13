# WAP to remove characters at even index number.

s = input("Enter your string : ")

if len(s)<=1:
    print(s)

else:
    print(s[1::2])