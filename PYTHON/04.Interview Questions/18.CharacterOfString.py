# WAP to print the characters of a string present at even index number and odd index number 

s = input("Enter your string : ")

i = 0
print("Characters of a string present at even index number:")

while i<len(s):
    if i%2 == 0:
        print(s[i])
    i=i+2

j = 1
print("Characters of a string present at odd index number:")
while j<len(s):
    if j%2 != 0:
        print(s[j])
    j=j+2

    
