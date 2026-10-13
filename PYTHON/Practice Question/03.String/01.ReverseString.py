# Write a program to reverse a given string
def get_reverse_string(str1):
    rev = ""
    for i in range(len(str1)-1, -1, -1):
        rev+=str1[i]
    print(f"Reverse string is : {rev}")


str1 = input("Enter the string : ")
get_reverse_string(str1)