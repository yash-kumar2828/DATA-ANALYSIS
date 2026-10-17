''' Write a program to reverse a given string
Input: hello
Output: olleh  '''


def get_reverse_string(str1):
    rev = ""
    for i in range(len(str1)-1, -1, -1):
        rev+=str1[i]
    print(f"Reverse string is : {rev}")


def get_reverse_string2(str1):
    rev = ""
    for i in str1:
        rev = i+rev

    print(f"The reverse string is : {rev}")


str1 = input("Enter the string : ")
get_reverse_string(str1)
get_reverse_string2(str1)