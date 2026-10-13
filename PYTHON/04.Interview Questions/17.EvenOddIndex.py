# WAP to print the characters of a string present at even index number and odd index number.
# I/P :- Holiday
# O/P :- Characters present at even index no. is : Hldy
#        Characters present at odd index no. is : oia

s = input("Enter your string : ")

print(f"Characters present at even index no. is : {s[::2]}")
print(f"Characters present at even index no. is : {s[1::2]}")