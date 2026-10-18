'''Check if a String Contains Only Alphabets
Input: Hello
Output: True'''


def check_only_alphabets(s1):

    res = s1.isalpha()

    print(res)


str1 = input("Enter the string : ")
check_only_alphabets(str1)