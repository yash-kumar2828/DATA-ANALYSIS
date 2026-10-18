'''Count Uppercase and Lowercase Characters
Input: Hello World
Output: Uppercase: 2, Lowercase: 8
'''


def get_uppercase_lowercase(s1):

    uppercase = 0
    lowercase = 0

    for i in s1:

        if i.isalpha() and i.isupper():
            uppercase+=1

        elif i.isalpha() and i.islower():
            lowercase+=1

    print(f"Uppercase : {uppercase}, Lowercase : {lowercase}")


s1 = input("Enter the string : ")
get_uppercase_lowercase(s1)