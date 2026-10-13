# Check if a String is Palindrome

def is_palidrome(str):
    rev = ""
    for i in range(len(str)-1, -1, -1):
        rev+=str[i]
    return str == rev 

str1 = input("Enter your string : ")

if is_palidrome(str1):
    print(f"{str1} is palidrome string")
else:
    print(f"{str1} is not palidrome string")