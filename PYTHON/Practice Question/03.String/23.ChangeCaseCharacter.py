'''Change Case of Each Character
Input: javA
Output: JAVa  '''

def change_case_character(str1):
    res = ''

    for i in str1:
        if i.isalpha() and i.islower():
            res = res+i.upper()

        elif i.isalpha() and i.isupper():
            res = res+i.lower()

        else:
            res = res+i

    print(res)


str1 = input("Enter the string : ")
change_case_character(str1)